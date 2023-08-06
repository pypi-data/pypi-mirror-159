"""Contains frame versions structure parser."""
from __future__ import annotations

from typing import Final, Optional, Tuple

from pyplumio import util
from pyplumio.helpers.typing import Records, Versions

FRAME_VERSIONS: Final = "frames"


def from_bytes(
    message: bytearray, offset: int = 0, data: Optional[Records] = None
) -> Tuple[Records, int]:
    """Parse bytes and return message data and offset."""
    if data is None:
        data = {}

    versions: Versions = {}
    frames_number = message[offset]
    offset += 1
    for _ in range(frames_number):
        frame_type = message[offset]
        version = util.unpack_ushort(message[offset + 1 : offset + 3])
        versions[frame_type] = version
        offset += 3

    data[FRAME_VERSIONS] = versions

    return data, offset
