"""
YouBit: using YouTube as a very slow but free file hosting service.
"""
from importlib.metadata import version
__title__ = "youbit"
__version__ = version("youbit")
__author__ = "Florian Laporte <florianl@florianl.dev>"
__license__ = "MIT License"

from .yb import Encoder, Decoder
from . import encode
from . import decode
from . import util
from . import video
from . import upload
from . import download
from .ecc import ecc

__all__ = [
    "Encoder",
    "Decoder",
    "encode",
    "decode",
    "download",
    "upload",
    "video",
    "util",
    "ecc",
]
