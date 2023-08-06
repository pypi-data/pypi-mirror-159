"""Contains protocol representation."""
from __future__ import annotations

import asyncio
import logging
from typing import Awaitable, Callable, Dict, Final, Optional, Tuple

from pyplumio.const import ATTR_NETWORK, ECOMAX_ADDRESS
from pyplumio.devices import Device, get_device_handler
from pyplumio.exceptions import (
    FrameError,
    ReadError,
    UnknownDeviceError,
    UnknownFrameError,
)
from pyplumio.frames import RequestTypes
from pyplumio.frames.requests import StartMaster
from pyplumio.helpers.factory import factory
from pyplumio.helpers.network_info import (
    EthernetParameters,
    NetworkInfo,
    WirelessParameters,
)
from pyplumio.helpers.task_manager import TaskManager
from pyplumio.stream import FrameReader, FrameWriter

_LOGGER = logging.getLogger(__name__)

CONSUMERS_NUMBER: Final = 2


def _get_device_handler_and_name(address: int) -> Tuple[str, str]:
    """Get device handler full path and lowercased class name."""
    handler = get_device_handler(address)
    _, class_name = handler.rsplit(".", 1)
    return handler, class_name.lower()


def _empty_queue(queue: asyncio.Queue) -> None:
    """Empty asyncio queue."""
    for _ in range(queue.qsize()):
        queue.get_nowait()
        queue.task_done()


class Protocol(TaskManager):
    """Represents protocol."""

    writer: Optional[FrameWriter]
    reader: Optional[FrameReader]
    devices: Dict[str, Device]
    _network: NetworkInfo
    _queues: Tuple[asyncio.Queue, asyncio.Queue]
    _connection_lost_callback: Optional[Callable[[], Awaitable[None]]]
    _closing: bool = False

    def __init__(
        self,
        connection_lost_callback: Optional[Callable[[], Awaitable[None]]] = None,
        ethernet_parameters: Optional[EthernetParameters] = None,
        wireless_parameters: Optional[WirelessParameters] = None,
    ):
        """Initialize new Protocol object."""
        super().__init__()
        self.writer = None
        self.reader = None
        self.devices = {}
        read_queue: asyncio.Queue = asyncio.Queue()
        write_queue: asyncio.Queue = asyncio.Queue()
        self._queues = (read_queue, write_queue)
        self._connection_lost_callback = connection_lost_callback
        if ethernet_parameters is None:
            ethernet_parameters = EthernetParameters()

        if wireless_parameters is None:
            wireless_parameters = WirelessParameters()

        self._network = NetworkInfo(eth=ethernet_parameters, wlan=wireless_parameters)

    def __getattr__(self, name: str):
        """Return attributes from the underlying devices table."""
        if name in self.devices:
            return self.devices[name]

        raise AttributeError

    async def frame_producer(
        self, read_queue: asyncio.Queue, lock: asyncio.Lock
    ) -> None:
        """Handle frame reads."""
        while self.reader:
            try:
                async with lock:
                    read_queue.put_nowait(await self.reader.read())
            except UnknownFrameError as e:
                _LOGGER.debug("UnknownFrameError: %s", e)
            except ReadError as e:
                _LOGGER.debug("ReadError: %s", e)
            except FrameError as e:
                _LOGGER.warning("FrameError: %s", e)
            except (ConnectionError, asyncio.TimeoutError):
                break

        self.create_task(self.connection_lost())

    async def frame_consumer(
        self, read_queue: asyncio.Queue, write_queue: asyncio.Queue
    ) -> None:
        """Handle frame processing."""
        while True:
            frame = await read_queue.get()
            try:
                handler, name = _get_device_handler_and_name(frame.sender)

                if name not in self.devices:
                    device = factory(handler, queue=write_queue)
                    self.devices[name] = device
                    self.set_event(name)

                self.devices[name].handle_frame(frame)

                if frame.is_type(
                    RequestTypes.CHECK_DEVICE, RequestTypes.PROGRAM_VERSION
                ):
                    response = frame.response(data={ATTR_NETWORK: self._network})
                    write_queue.put_nowait(response)

            except UnknownDeviceError as e:
                _LOGGER.debug("UnknownDeviceError: %s", e)

            read_queue.task_done()

    async def write_consumer(
        self, write_queue: asyncio.Queue, lock: asyncio.Lock
    ) -> None:
        """Handle frame writes."""
        while self.writer:
            frame = await write_queue.get()
            try:
                async with lock:
                    await self.writer.write(frame)
            except (ConnectionError, asyncio.TimeoutError):
                break

            write_queue.task_done()

        self.create_task(self.connection_lost())

    def connection_established(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ):
        """Start consumers and producer tasks."""
        self.reader = FrameReader(reader)
        self.writer = FrameWriter(writer)
        read_queue, write_queue = self.queues
        write_queue.put_nowait(StartMaster(recipient=ECOMAX_ADDRESS))
        lock: asyncio.Lock = asyncio.Lock()
        self.create_task(self.write_consumer(write_queue, lock))
        self.create_task(self.frame_producer(read_queue, lock))
        for _ in range(CONSUMERS_NUMBER):
            self.create_task(self.frame_consumer(*self.queues))

    async def connection_lost(self):
        """Shutdown consumers and call connection lost callback."""
        for queue in self.queues:
            _empty_queue(queue)

        self.writer = None
        self.reader = None
        await self.shutdown()
        if self._connection_lost_callback is not None:
            await self._connection_lost_callback()

    async def shutdown(self):
        """Shutdown protocol tasks."""
        await asyncio.wait([queue.join() for queue in self.queues])
        tasks = [task for task in self.tasks if not task == asyncio.current_task()]
        for task in tasks:
            task.cancel()

        await asyncio.gather(*tasks, return_exceptions=True)
        if self.writer:
            await self.writer.close()

        for device in self.devices.values():
            await device.shutdown()

    async def get_device(self, device: str) -> Device:
        """Wait for device and return it once it's available."""
        if device not in self.devices:
            await self.create_event(device).wait()

        return self.devices[device]

    @property
    def queues(self) -> Tuple[asyncio.Queue, asyncio.Queue]:
        """Return protocol queues."""
        return self._queues
