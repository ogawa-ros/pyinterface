

__version__ = '1.6.0'

interface_vendor_id = 0x1147

try:
    from .tools import open
    from .tools import lspci
    from .core import interface_driver
except ModuleNotFoundError:
    pass
