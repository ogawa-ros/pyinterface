

__version__ = '0.4.5'


try:
    from .tools import open
    
    from .core import interface_driver
    
    from . import pci2702
    from . import pci2724
    from . import pci3165
    from . import pci3177
    from . import pci3342
    from . import pci340516
    from . import pci340816
    from . import pci6204
    from . import pci7204
    
except:
    pass
