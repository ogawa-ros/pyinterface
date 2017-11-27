
import copy
import collections
import logging
import portio

loglevel = logging.INFO


# definitions
# ===========

# exceptions
# ----------
class BadMemoryAccessError(Exception):
    def __init__(self, message):
        self.message = message
        pass

# namedtuples
# -----------
BoardInfo = collections.namedtuple('BoardInfo',
                                   ['slot', 'device_class', 'vendor',
                                    'device', 'svendor', 'sdevice', 'rev',
                                    'port', 'dump', 'text'])

PortInfo = collections.namedtuple('PortInfo',
                                  ['addr', 'addr16', 'size'])


# class
# -----
class Bytes(object):
    data = []
    
    def __init__(self, data=[], addr=0x00):
        if data != []:
            self.data = data
        else:
            self.data = copy.deepcopy(self.data)
            pass

        for i, d in enumerate(self.data):
            if 'addr' not in d: d['addr'] = addr + i
            if 'byte' not in d: d['byte'] = b'\x00'
            continue
        
        self.size = len(self.data)
        self.start_addr = self.data[0]['addr']
        pass

    def __int__(self):
        return self.int()
    
    def __repr__(self):
        return self.hex()

    def __str__(self):
        return self.hex()

    def __eq__(self, val):
        return self.int() == val

    def __and__(self, val):
        return self.int() & val
    
    def __or__(self, val):
        return self.int() | val
    
    def __xor__(self, val):
        return self.int() ^ val
    
    def __getitem__(self, key):
        if isinstance(key, str):
            for byte in self:
                for i, name in enumerate(byte.data[0]['name']):
                    if key == name:
                        return int(byte.bin()[-(i+1)])
                    continue
                continue
            return None
        
        if isinstance(key, slice):
            new_d = self.data[key]
        else:
            new_d = [self.data[key],]
            pass
        new_bytes = Bytes(copy.deepcopy(new_d))
        return new_bytes
    
    def int(self):
        return int.from_bytes(self.bytes(), 'little')

    def bytes(self):
        return b''.join([d['byte'] for d in self.data])

    def hex(self):
        return ''.join([format(b, '02X') for b in self.bytes()])
    
    def bin(self):
        return ''.join([format(b, '08b') for b in self.bytes()])
    
    def bit(self, bit):
        if type(bit) == int: return self.int() & 2**bit
        
        if type(bit) == str:
            for j, d in enumerate(self.data):
                for i, name in enumerate(d['name']):
                    if name == bit: return (d['byte'][0] & 2**i) * 2**(8*j)
                    continue
                continue
            pass
        return
    
    def ordered_bit(self):
        return ''.join([format(b, '08b')[::-1] for b in self.bytes()])
    
    def ordered_bit_names(self):
        names = []
        for d in self.data:
            for name in d['name']:
                names.append(name)
                continue
            continue
        return names
    
    def print(self):
        msg = '%s\n\n'%(object.__repr__(self))
        
        for i, d in enumerate(self.data):
            byte = int.from_bytes(d['byte'], 'little')
            bits1 = format(byte, '08b')
            bits2 = bits1[::-1]
            addr = d['addr']
            msg += 'Address 0x{addr:02X} : '.format(**locals())
            msg += 'value = 0x{byte:02X} (0b{bits1})\n'.format(**locals())
            for j, (bit, name) in enumerate(zip(bits2, d['name'])):
                if name == '':
                    msg += '  {j} : {bit}\n'.format(**locals())
                else:
                    msg += '  {j} : {name} = {bit}\n'.format(**locals())
                    pass
                continue
            msg += '\n'
            continue
        
        print(msg)
        return
    
    def set(self, value):
        if type(value) == int: self.set_by_int(value)
        elif type(value) in [str, list, tuple]: self.set_by_str(value)
        elif type(value) == Bytes: self.set_by_bytes(value)
        return
    
    def set_by_int(self, value):
        bytes_ = value.to_bytes(self.size, 'little')
        for i, byte in enumerate(bytes_):
            self.data[i]['byte'] = byte.to_bytes(1, 'little')
            continue
        return
    
    def set_by_str(self, values):
        if type(values) == str:
            values = values.replace(' ', ',').split(',')
            pass

        values = [v for v in values if v!='']
        
        for data_ind in range(self.size):
            byte = 0
            for bit_ind in range(8):
                if self.data[data_ind]['name'][bit_ind] in values:
                    byte += 2**bit_ind
                    pass
                continue
            self.data[data_ind]['byte'] = byte.to_bytes(1, 'little')
            continue
        return
    
    def set_by_bytes(self, value):
        for d in value.data:
            for i in range(len(self.data)):
                if d['addr'] == self.data[i]['addr']:
                    self.data[i] = copy.deepcopy(d)
                    pass
                continue
            continue
        return
    
    def bit_on(self, bits):
        if type(bits) == str:
            bits = bits.replace(' ', ',').split(',')
            pass
        
        bits = [b for b in bits if b!='']
        
        for data_ind in range(self.size):
            mask_on = 0
            for bit_ind in range(8):
                if self.data[data_ind]['name'][bit_ind] in bits:
                    mask_on += 2**bit_ind
                    pass
                continue
            original = int.from_bytes(self.data[data_ind]['byte'], 'little')
            masked = original | mask_on
            self.data[data_ind]['byte'] = masked.to_bytes(1, 'little')
            continue
        return
            
    def bit_off(self, bits):
        if type(bits) == str:
            bits = bits.replace(' ', ',').split(',')
            pass
        
        bits = [b for b in bits if b!='']
        
        for data_ind in range(self.size):
            mask_off = 0
            for bit_ind in range(8):
                if not self.data[data_ind]['name'][bit_ind] in bits:
                    mask_off += 2**bit_ind
                    pass
                continue
            original = int.from_bytes(self.data[data_ind]['byte'], 'little')
            masked = original & mask_off
            self.data[data_ind]['byte'] = masked.to_bytes(1, 'little')
            continue
        return
            
    
class interface_driver(object):
    config = None
    bytes_in = []
    bytes_out = []
    
    def __init__(self, config, logger=None):
        if logger is None:
            logger = logging.getLogger(__package__+'.'+__name__)
            logger.setLevel(loglevel)
            logger.propagate = False
            loghandler = logging.StreamHandler()
            loghandler.setLevel(loglevel)
            loghandler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
            logger.addHandler(loghandler)
            pass
        self.logger = logger
        
        self.config = config
        self.bid = self._get_board_id()
        pass

    def initialize(self):
        pass
    
    def read(self, target):
        ret = self._read(target.start_addr, target.size)
        target.set(ret)
        [in_.set(target) for in_ in self.bytes_in]
        return target
    
    def _read(self, addr, size=1):
        self.validate_memory_access(addr, size)
        self.logger.debug('read {0}-{1}'.format(hex(addr), hex(addr+size-1)))
        if size == 1: return portio.inb(addr)
        if size == 2: return portio.inw(addr)
        if size == 4: return portio.inl(addr)
        return
    
    def write(self, target):
        ret = self._write(target.int(), target.start_addr, target.size)
        [out_.set(target) for out_ in self.bytes_out]
        return target
    
    def _write(self, data, addr, size):
        self.validate_memory_access(addr, size)
        self.logger.debug('write {0}-{1}'.format(hex(addr), hex(addr+size-1)))
        if size == 1: return portio.outb(data, addr)
        if size == 2: return portio.outw(data, addr)
        if size == 4: return portio.outl(data, addr)
        return

    def validate_memory_access(self, addr, size):
        if size not in [1, 2, 4]:
            msg = 'size should be 1, 2, or 4'
            msg += ' while {0} is given.'.format(size)
            raise BadMemoryAccessError(msg)
        
        start_addr = addr
        stop_addr = addr + size - 1
        
        valid_ranges = [[p.addr, p.addr+p.size-1] for p in self.config.port]        
        validation = []
        for vr0, vr1 in valid_ranges:
            if (vr0 <= start_addr <= vr1) and (vr0 <= stop_addr <= vr1):
                validation.append(1)
            else:
                validation.append(0)
                pass
            continue
        
        if sum(validation) == 0:
            addr_spaces = ', '.join(['{0}-{1}'.format(hex(vr0), hex(vr1))
                                     for vr0, vr1 in valid_ranges])
            msg = 'I/O addr space is {0}'.format(addr_spaces)
            msg += ' while tried to access {0}-{1}.'.format(hex(start_addr),
                                                            hex(stop_addr))
            raise BadMemoryAccessError(msg)
        
        return

