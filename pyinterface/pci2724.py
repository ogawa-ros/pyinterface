
from .core import interface_driver
from .core import Bytes


class InvalidIoNumberError(Exception):
    def __init__(self, message):
        self.message = message
        pass

class InvalidListLengthError(Exception):
    def __init__(self, message):
        self.message = message
        pass

    
class pci2724_in(Bytes):
    data = [
        {'name': ['IN1', 'IN2', 'IN3', 'IN4', 'IN5', 'IN6', 'IN7', 'IN8']},
        {'name': ['IN9', 'IN10', 'IN11', 'IN12', 'IN13', 'IN14', 'IN15', 'IN16']},
        {'name': ['IN17', 'IN18', 'IN19', 'IN20', 'IN21', 'IN22', 'IN23', 'IN24']},
        {'name': ['IN25', 'IN26', 'IN27', 'IN28', 'IN29', 'IN30', 'IN31', 'IN32']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['IRIN2', '', '', '', '', 'STB2', 'ACKR2', 'ACK2']},
        {'name': ['IRIN1', '', '', '', 'LF', 'ACK1', 'STBR1', 'STB1']},
        {'name': ['TD1', 'TD2', 'TD3', 'TD4', '', '', '', '']},
        {'name': ['PORT0', 'PORT1', 'PORT2', 'PORT3', '', '', '', '']},
        {'name': ['SIG1', 'SIG2', 'SIG3', 'SIG4', 'SIGT', 'SIGR', 'SIGRR', '']},
        {'name': ['SIG1', 'SIG2', 'SIG3', 'SIG4', 'SIGT', 'SIGR', '', '']},
        {'name': ['SIG1', 'SIG2', 'SIG3', 'SIG4', 'EDS1', 'EDS2', 'EDS3', 'EDS4']},
        {'name': ['BID0', 'BID1', 'BID2', 'BID3', '', '', '', '']},
    ]
        
class pci2724_out(Bytes):
    data = [
        {'name': ['OUT1', 'OUT2', 'OUT3', 'OUT4', 'OUT5', 'OUT6', 'OUT7', 'OUT8']},
        {'name': ['OUT9', 'OUT10', 'OUT11', 'OUT12', 'OUT13', 'OUT14', 'OUT15', 'OUT16']},
        {'name': ['OUT17', 'OUT18', 'OUT19', 'OUT20', 'OUT21', 'OUT22', 'OUT23', 'OUT24']},
        {'name': ['OUT25', 'OUT26', 'OUT27', 'OUT28', 'OUT29', 'OUT30', 'OUT31', 'OUT32']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', 'PO10', 'PO11', 'PO12', 'ACK10', 'ACK11']},
        {'name': ['', '', '', 'PO20', 'PO21', 'PO22', 'STB20', 'STB21']},
        {'name': ['TCTRL1', 'TCTRL2', 'TCTRL3', 'TCTRL4', 'SCK1', 'SCK2', 'SCK3', '']},
        {'name': ['PORT0', 'PORT1', 'PORT2', 'PORT3', '', '', '', '']},
        {'name': ['SIG1', 'SIG2', 'SIG3', 'SIG4', 'SIGT', 'SIGR', '', '']},
        {'name': ['SIG1', 'SIG2', 'SIG3', 'SIG4', 'SIGT', 'SIGR', '', '']},
        {'name': ['SIG1', 'SIG2', 'SIG3', 'SIG4', 'EDS1', 'EDS2', 'EDS3', 'EDS4']},
        {'name': ['', '', '', '', '', '', '', '']},
    ]

    
class pci2724_driver(interface_driver):
    io_number = 32
    
    def __init__(self, config):
        self.bytes_in = [pci2724_in(addr=config.port[0].addr)]
        self.bytes_out = [pci2724_out(addr=config.port[0].addr)]
        super().__init__(config)
        pass

    def _get_board_id(self):
        return self.read(self.bytes_in[0][0x0f])
    
    def _get_register(self, addr, size=1):
        target = self.bytes_in[0][addr:addr+size]
        return self.read(target)
    
    def _set_register(self, addr, data, size=1):
        target = self.bytes_out[0][addr:addr+size]
        target.set(data)
        return self.write(target)

    def _get_out_chache(self, addr, size=1):
        return self.bytes_out[0][addr:addr+size]

    def _verify_io_number_access(self, start, num):
        if (start < 1) or (start+num > self.io_number+1):
            msg = 'I/O number should be 1-{0}'.format(self.io_number)
            msg += ' while {0}-{1} is given.'.format(start, start+num-1)
            raise InvalidIoNumberError(msg)
        return
    
    def _get_input(self):
        return self._get_register(0x00, 4)
    
    def _set_output(self, data, start):
        num = len(data)
        start_ = start - 1
        stop_ = start_ + num
        
        self._verify_io_number_access(start, num)
        outp = self._get_out_chache(0x00, 4)
        names = outp.ordered_bit_names()
        for d, name in zip(data, names[start_:stop_]):
            if d == 1: outp.bit_on(name)
            else: outp.bit_off(name)
            continue
        return self._set_register(0x00, outp, 4)
    
    def initialize(self):
        self.bytes_in[0].set(0)
        self.bytes_out[0].set(0)
        self.output_dword([0]*32)
        self.set_latch_status()
        return

    def input_point(self, start, num):
        """
        Compatibility: DioInputPoint function in GPG-2000 driver
        """
        self._verify_io_number_access(start, num)
        inp = self._get_input()
        bits_str = inp.ordered_bit()
        bits = list(map(int, bits_str[start-1:start+num-1]))
        return bits

    def output_point(self, data, start_num):
        """
        Compatibility: DioOutputPoint function in GPG-2000 driver
        """
        return self._set_output(data, start_num)

    def input_byte(self, num):
        """
        Compatibility: DioInputByte function in GPG-2000 driver
        """
        if isinstance(num, str):
            if num.find('IN1_8') != -1: num = 1
            elif num.find('IN9_16') != -1: num = 9
            elif num.find('IN17_24') != -1: num = 17
            elif num.find('IN25_32') != -1: num = 25
            else: return
            
        self._verify_io_number_access(num, 8)
        inp = self._get_input()
        bits_str = inp.ordered_bit()
        bits = list(map(int, bits_str[num-1:num+8-1]))
        return bits
    
    def input_word(self, num):
        """
        Compatibility: DioInputWord function in GPG-2000 driver
        """
        if isinstance(num, str):
            if num.find('IN1_16') != -1: num = 1
            elif num.find('IN17_32') != -1: num = 17
            else: return
            
        self._verify_io_number_access(num, 16)
        inp = self._get_input()
        bits_str = inp.ordered_bit()
        bits = list(map(int, bits_str[num-1:num+16-1]))
        return bits

    def input_dword(self):
        """
        Compatibility: DioInputDword function in GPG-2000 driver
        """
        self._verify_io_number_access(1, 32)
        inp = self._get_input()
        bits_str = inp.ordered_bit()
        bits = list(map(int, bits_str[0:32]))
        return bits

    def output_byte(self, data, num):
        """
        Compatibility: DioOutputByte function in GPG-2000 driver
        """
        if len(data) != 8:
            msg = 'data length should be 8'
            msg += ' while {0} length list is given.'.format(len(data))
            raise InvalidListLengthError(msg)
        
        if isinstance(num, str):
            if num.find('OUT1_8') != -1: num = 1
            elif num.find('OUT9_16') != -1: num = 9
            elif num.find('OUT17_24') != -1: num = 17
            elif num.find('OUT25_32') != -1: num = 25
            else: return
            
        return self._set_output(data, num)

    def output_word(self, data, num):
        """
        Compatibility: DioOutputWord function in GPG-2000 driver
        """
        if len(data) != 16:
            msg = 'data length should be 16'
            msg += ' while {0} length list is given.'.format(len(data))
            raise InvalidListLengthError(msg)
        
        if isinstance(num, str):
            if num.find('OUT1_16') != -1: num = 1
            elif num.find('OUT17_32') != -1: num = 17
            else: return
            
        return self._set_output(data, num)

    def output_dword(self, data):
        """
        Compatibility: DioOutputDword function in GPG-2000 driver
        """
        if len(data) != 32:
            msg = 'data length should be 32'
            msg += ' while {0} length list is given.'.format(len(data))
            raise InvalidListLengthError(msg)
        
        return self._set_output(data, 1)
    
    def set_latch_status(self, enable=''):
        """
        Compatibility: DioSetLatchStatus function in GPG-2000 driver
        
        Parameters
        ----------
        enable : str ('PORT0', 'PORT1', 'PORT2' and/or 'PORT3')
            'PORT0' = IN1 - IN8
            'PORT1' = IN9 - IN16
            'PORT2' = IN17 - IN24
            'PORT3' = IN25 - IN32
        
        Examples
        --------
        b.set_latch_status('PORT0 PORT3')
        """
        addr = 0x0b
        flags = enable
        return self._set_register(addr, flags)
    
    def get_latch_status(self):
        """
        Compatibility: DioGetLatchStatus function in GPG-2000 driver
        """
        addr = 0x0b
        return self._get_register(addr)
    
    def get_ack_status(self):
        """
        Compatibility: DioGetAckStatus function in GPG-2000 driver
        """
        addr = 0x08
        return self._get_register(addr)
    
    def set_ack_pulse_command(self, ack='', pulse=''):
        """
        Compatibility : DioSetAckPulseCommand function in GPG-2000 driver
        
        Parameters
        ----------
        ack : str ('ACK10' or 'ACK11')
            ''      = do nothing
            'ACK10' = clear ACK1 terminal (Low -> High)
            'ACK11' = set ACK1 terminal (High -> Low)
        
        pulse : str ('PO10', 'PO11' or 'PO12')
            ''     = do nothing
            'PO10' = set PULS.OUT1 terminal High
            'PO11' = set PULS.OUT1 terminal Low
            'PO12' = output Low pulse from PULS.OUT1 terminal
        """
        addr = 0x08
        flags = ack + ' ' + pulse
        return self._set_register(addr, flags)
    
    def get_stb_status(self):
        """
        Compatibility: DioGetStbStatus function in GPG-2000 driver
        """
        addr = 0x09
        return self._get_register(addr)
        
    def set_stb_pulse_command(self, stb='', pulse=''):
        """
        Compatibility : DioSetStbPulseCommand function in GPG-2000 driver
        
        Parameters
        ----------
        stb : str ('STB20' or 'STB21')
            ''      = do nothing
            'STB20' = clear STB2 terminal (Low -> High)
            'STB21' = set STB2 terminal (High -> Low)
        
        pulse : str ('PO20', 'PO21' or 'PO22')
            ''     = do nothing
            'PO20' = set PULS.OUT2 terminal High
            'PO21' = set PULS.OUT2 terminal Low
            'PO22' = output Low pulse from PULS.OUT2 terminal
        """
        addr = 0x09
        flags = stb + ' ' + pulse
        return self._set_register(addr, flags)

    
