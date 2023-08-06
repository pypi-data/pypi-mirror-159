__author__ = "filesystem"
__copyright__ = "Copyright 2022-present CantCode"
__version__ = "0.0.1"

import logging
from typing import NamedTuple

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .main import Money

class VersionInfo(NamedTuple):
    """
    Represents the package's version info.
    """
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=2,
    minor=0,
    micro=0,
    releaselevel="release",
    serial=0
)

logging.getLogger(__name__).addHandler(logging.NullHandler())