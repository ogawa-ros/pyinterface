try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

try:
    __version__ = version("pyinterface")
except:
    __version__ = "0.0.0"


interface_vendor_id = 0x1147


from .tools import open
from .tools import lspci
from .core import interface_driver

