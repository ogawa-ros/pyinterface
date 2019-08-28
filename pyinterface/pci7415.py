
import struct
import time
from . import core

# functions
# =========

def to_comp28_format(x):
    data = [struct.pack('I', i & 0xffffffff) for i in x]
    return data

def to_comp16_format(x):
    data = [struct.pack('<I', i & 0xffff) for i in x]
    return data

def to_byte_format(x):
    data = [struct.pack('<I', i) for i in x]
    return data

def to_prmd_format(x):
    pass

def to_prip_format(x):
    data = [struct.pack('<I', i & 0xfffffff) for i in x]
    return data

def from_comp28_format(x):
    data = []
    for i in x:
        a = i.to_bit()[0:28][::-1]
        b = -int(a[0]) << len(a) | int(a, 2)
        data.append(b)
    return data

def from_comp16_format(x):
    data = []
    for i in x:
        a = i.to_bit()[0:16][::-1]
        b = -int(a[0]) << len(a) | int(a, 2)
        data.append(b)
    return data

def from_byte_format(x):
    data = [i.to_int() for i in x]
    return data

def from_rpls_format(x):
    data = []
    for i in x:
        a = i.to_bit()[0:28][::-1]
        b = -int(a[0]) << len(a) | int(a, 2)
        data.append(b)
    return data

def do_nothing(x):
    return x


class pci7415_driver(core.interface_driver):
    bit_flags_in = (
        (
            ('TD1', 'TD2', 'TD3', 'TD4', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('DI1', 'DI2', 'DI3', 'DI4', 'DI5', 'DI6', 'DI7', 'DI8'),
            ('DI9', 'DI10', 'DI11', 'DI12', '', '', '', ''),
            ('ELL1', 'ELL2', 'ELL3', 'ELL4', '', '', '', ''),
            ('SIGC', 'SIGT', 'SIGR', 'SIGI', '', '', '', ''),
            ('', 'MIRT', 'MIRR', 'MIRI', '', '', '', ''),
            ('LOCK', 'EXTRST', 'LOCKRST', '', '', '', '', ''),
            ('CLKMODE0', 'CLKMODE1', '', '', '', '', '', ''),
            ('AUTOBUSY', 'STEPBUSY', 'STEPMODE', '', 'ROMBUSY', '', '', ''),
            ('ND0', 'ND1', 'ND2', 'ND3', 'ND4', 'ND5', 'ND6', 'ND7'),
            ('ND8', 'ND9', 'ND10', 'ND11', '', '', '', ''),
            ('ED0', 'ED1', 'ED2', 'ED3', 'ED4', 'ED5', 'ED6', 'ED7'),
            ('ED8', 'ED9', 'ED10', 'ED11', '', '', '', ''),
            ('SYNCLINE0', 'SYNCLINE1', 'SYNCLINE2', '', 'SIGSEL', '', '', 'RD'),
            ('BID0', 'BID1', 'BID2', 'BID3', '', '', '', '')
        ),
        (
            ('SSCM', 'SRUN', 'SENI', 'SEND', 'SERR', 'SINT', 'SSC0', 'SSC1'),
            ('SCP1', 'SCP2', 'SCP3', 'SCP4', 'SCP5', 'SEOR', 'SPRF', 'SPDF'),
            ('IOP0', 'IOP1', 'IOP2', 'IOP3', 'IOP4', 'IOP5', 'IOP6', 'IOP7'),
            ('SFU', 'SFD', 'SFC', 'SALM', 'SPEL', 'SMEL', 'SORG', 'SSD'),
            ('BUFB00', 'BUFB01', 'BUFB02', 'BUFB03', 'BUFB04', 'BUFB05', 'BUFB06', 'BUFB07'),
            ('BUFB10', 'BUFB11', 'BUFB12', 'BUFB13', 'BUFB14', 'BUFB15', 'BUFB16', 'BUFB17'),
            ('BUFB20', 'BUFB21', 'BUFB22', 'BUFB23', 'BUFB24', 'BUFB25', 'BUFB26', 'BUFB27'),
            ('BUFB30', 'BUFB31', 'BUFB32', 'BUFB33', 'BUFB34', 'BUFB35', 'BUFB36', 'BUFB37'),
            ('SSCM', 'SRUN', 'SENI', 'SEND', 'SERR', 'SINT', 'SSC0', 'SSC1'),
            ('SCP1', 'SCP2', 'SCP3', 'SCP4', 'SCP5', 'SEOR', 'SPRF', 'SPDF'),
            ('IOP0', 'IOP1', 'IOP2', 'IOP3', 'IOP4', 'IOP5', 'IOP6', 'IOP7'),
            ('SFU', 'SFD', 'SFC', 'SALM', 'SPEL', 'SMEL', 'SORG', 'SSD'),
            ('BUFB00', 'BUFB01', 'BUFB02', 'BUFB03', 'BUFB04', 'BUFB05', 'BUFB06', 'BUFB07'),
            ('BUFB10', 'BUFB11', 'BUFB12', 'BUFB13', 'BUFB14', 'BUFB15', 'BUFB16', 'BUFB17'),
            ('BUFB20', 'BUFB21', 'BUFB22', 'BUFB23', 'BUFB24', 'BUFB25', 'BUFB26', 'BUFB27'),
            ('BUFB30', 'BUFB31', 'BUFB32', 'BUFB33', 'BUFB34', 'BUFB35', 'BUFB36', 'BUFB37'),
            ('SSCM', 'SRUN', 'SENI', 'SEND', 'SERR', 'SINT', 'SSC0', 'SSC1'),
            ('SCP1', 'SCP2', 'SCP3', 'SCP4', 'SCP5', 'SEOR', 'SPRF', 'SPDF'),
            ('IOP0', 'IOP1', 'IOP2', 'IOP3', 'IOP4', 'IOP5', 'IOP6', 'IOP7'),
            ('SFU', 'SFD', 'SFC', 'SALM', 'SPEL', 'SMEL', 'SORG', 'SSD'),
            ('BUFB00', 'BUFB01', 'BUFB02', 'BUFB03', 'BUFB04', 'BUFB05', 'BUFB06', 'BUFB07'),
            ('BUFB10', 'BUFB11', 'BUFB12', 'BUFB13', 'BUFB14', 'BUFB15', 'BUFB16', 'BUFB17'),
            ('BUFB20', 'BUFB21', 'BUFB22', 'BUFB23', 'BUFB24', 'BUFB25', 'BUFB26', 'BUFB27'),
            ('BUFB30', 'BUFB31', 'BUFB32', 'BUFB33', 'BUFB34', 'BUFB35', 'BUFB36', 'BUFB37'),
            ('SSCM', 'SRUN', 'SENI', 'SEND', 'SERR', 'SINT', 'SSC0', 'SSC1'),
            ('SCP1', 'SCP2', 'SCP3', 'SCP4', 'SCP5', 'SEOR', 'SPRF', 'SPDF'),
            ('IOP0', 'IOP1', 'IOP2', 'IOP3', 'IOP4', 'IOP5', 'IOP6', 'IOP7'),
            ('SFU', 'SFD', 'SFC', 'SALM', 'SPEL', 'SMEL', 'SORG', 'SSD'),
            ('BUFB00', 'BUFB01', 'BUFB02', 'BUFB03', 'BUFB04', 'BUFB05', 'BUFB06', 'BUFB07'),
            ('BUFB10', 'BUFB11', 'BUFB12', 'BUFB13', 'BUFB14', 'BUFB15', 'BUFB16', 'BUFB17'),
            ('BUFB20', 'BUFB21', 'BUFB22', 'BUFB23', 'BUFB24', 'BUFB25', 'BUFB26', 'BUFB27'),
            ('BUFB30', 'BUFB31', 'BUFB32', 'BUFB33', 'BUFB34', 'BUFB35', 'BUFB36', 'BUFB37')
        )
    )

    bit_flags_out = (
        (
            ('TCTRL1', 'TCTRL2', 'TCTRL3', 'TCTRL4', 'SCK1' ,'SCK2' ,'SCK3' ,''),
            ('', '', '', '', '', '', '', ''),
            ('DO1', 'DO2', 'DO3', 'DO4', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('ELL1', 'ELL2', 'EL3', 'ELL4', '', '', '', ''),
            ('SIGRCLR1', 'SIGRCLR2', 'SIGRCLR3', 'SIGRCLR4', 'SIGICLR1', 'SIGICLR2', 'SIGICLR3', 'SIGICLR4'),
            ('', 'MIRT', 'MIRR', 'MIRI', '', '', '', ''),
            ('', 'EXTRST', 'LOCKRST', '', '', '', '', ''),
            ('CLKMODE0', 'CLKMODE1', 'CSTAOUT', 'CSTPOUT', '', '', '', ''),
            ('AUTO', 'STEP', 'STEPMODE', '', '', '', '', ''),
            ('ND0', 'ND1', 'ND2', 'ND3', 'ND4', 'ND5', 'ND6', 'ND7'),
            ('ND8', 'ND9', 'ND10', 'ND11', '', '', '', ''),
            ('ED0', 'ED1', 'ED2', 'ED3', 'ED4', 'ED5', 'ED6', 'ED7'),
            ('ED8', 'ED9', 'ED10', 'ED11', '', '', '', ''),
            ('SYNCLINE0', 'SYNCLINE1', 'SYNCLINE2', '', 'SIGSEL', '', '', 'RD'),
            ('', '', '', '', '', '', '', '')
        ),
        (
            ('COMB00', 'COMB01', 'COMB02', 'COMB03', 'COMB04', 'COMB05', 'COMB06', 'COMB07'),
            ('SELx', 'SELy', 'SELz', 'SELu', '', '', '', ''),
            ('OTP0', 'OTP1', 'OTP2', 'OTP3', 'OTP4', 'OTP5', 'OTP6', 'OTP7'),
            ('', '', '', '', '', '', '', ''),
            ('BUFB00', 'BUFB01', 'BUFB02', 'BUFB03', 'BUFB04', 'BUFB05', 'BUFB06', 'BUFB07'),
            ('BUFB10', 'BUFB11', 'BUFB12', 'BUFB13', 'BUFB14', 'BUFB15', 'BUFB16', 'BUFB17'),
            ('BUFB20', 'BUFB21', 'BUFB22', 'BUFB23', 'BUFB24', 'BUFB25', 'BUFB26', 'BUFB27'),
            ('BUFB30', 'BUFB31', 'BUFB32', 'BUFB33', 'BUFB34', 'BUFB35', 'BUFB36', 'BUFB37'),
            ('COMB00', 'COMB01', 'COMB02', 'COMB03', 'COMB04', 'COMB05', 'COMB06', 'COMB07'),
            ('SELx', 'SELy', 'SELz', 'SELu', '', '', '', ''),
            ('OTP0', 'OTP1', 'OTP2', 'OTP3', 'OTP4', 'OTP5', 'OTP6', 'OTP7'),
            ('', '', '', '', '', '', '', ''),
            ('BUFB00', 'BUFB01', 'BUFB02', 'BUFB03', 'BUFB04', 'BUFB05', 'BUFB06', 'BUFB07'),
            ('BUFB10', 'BUFB11', 'BUFB12', 'BUFB13', 'BUFB14', 'BUFB15', 'BUFB16', 'BUFB17'),
            ('BUFB20', 'BUFB21', 'BUFB22', 'BUFB23', 'BUFB24', 'BUFB25', 'BUFB26', 'BUFB27'),
            ('BUFB30', 'BUFB31', 'BUFB32', 'BUFB33', 'BUFB34', 'BUFB35', 'BUFB36', 'BUFB37'),
            ('COMB00', 'COMB01', 'COMB02', 'COMB03', 'COMB04', 'COMB05', 'COMB06', 'COMB07'),
            ('SELx', 'SELy', 'SELz', 'SELu', '', '', '', ''),
            ('OTP0', 'OTP1', 'OTP2', 'OTP3', 'OTP4', 'OTP5', 'OTP6', 'OTP7'),
            ('', '', '', '', '', '', '', ''),
            ('BUFB00', 'BUFB01', 'BUFB02', 'BUFB03', 'BUFB04', 'BUFB05', 'BUFB06', 'BUFB07'),
            ('BUFB10', 'BUFB11', 'BUFB12', 'BUFB13', 'BUFB14', 'BUFB15', 'BUFB16', 'BUFB17'),
            ('BUFB20', 'BUFB21', 'BUFB22', 'BUFB23', 'BUFB24', 'BUFB25', 'BUFB26', 'BUFB27'),
            ('BUFB30', 'BUFB31', 'BUFB32', 'BUFB33', 'BUFB34', 'BUFB35', 'BUFB36', 'BUFB37'),
            ('COMB00', 'COMB01', 'COMB02', 'COMB03', 'COMB04', 'COMB05', 'COMB06', 'COMB07'),
            ('SELx', 'SELy', 'SELz', 'SELu', '', '', '', ''),
            ('OTP0', 'OTP1', 'OTP2', 'OTP3', 'OTP4', 'OTP5', 'OTP6', 'OTP7'),
            ('', '', '', '', '', '', '', ''),
            ('BUFB00', 'BUFB01', 'BUFB02', 'BUFB03', 'BUFB04', 'BUFB05', 'BUFB06', 'BUFB07'),
            ('BUFB10', 'BUFB11', 'BUFB12', 'BUFB13', 'BUFB14', 'BUFB15', 'BUFB16', 'BUFB17'),
            ('BUFB20', 'BUFB21', 'BUFB22', 'BUFB23', 'BUFB24', 'BUFB25', 'BUFB26', 'BUFB27'),
            ('BUFB30', 'BUFB31', 'BUFB32', 'BUFB33', 'BUFB34', 'BUFB35', 'BUFB36', 'BUFB37')
        )
    )

    cmd_dict = {
        'write': {
            'rmv': {'cmd': 0x90, 'func': to_comp28_format},
            'rfl': {'cmd': 0x91, 'func': to_byte_format},
            'rfh': {'cmd': 0x92, 'func': to_byte_format},
            'rur': {'cmd': 0x93, 'func': to_byte_format},
            'rdr': {'cmd': 0x94, 'func': to_byte_format},
            'rmg': {'cmd': 0x95, 'func': to_byte_format},
            'rdp': {'cmd': 0x96, 'func': to_byte_format},
            'rmd': {'cmd': 0x97, 'func': to_prmd_format},
            'rip': {'cmd': 0x98, 'func': to_prip_format},
            'rus': {'cmd': 0x99, 'func': to_byte_format},
            'rds': {'cmd': 0x9A, 'func': to_byte_format},
            'renv1': {'cmd': 0x9C, 'func': to_byte_format},
            'prmv': {'cmd': 0x80, 'func': to_comp28_format},
            'prfl': {'cmd': 0x81, 'func': to_byte_format},
            'prfh': {'cmd': 0x82, 'func': to_byte_format},
            'prur': {'cmd': 0x83, 'func': to_byte_format},
            'prdr': {'cmd': 0x84, 'func': to_byte_format},
            'prmg': {'cmd': 0x85, 'func': to_byte_format},
            'prdp': {'cmd': 0x86, 'func': to_byte_format},
            'prmd': {'cmd': 0x87, 'func': to_byte_format},
            'prip': {'cmd': 0x88, 'func': to_prip_format},
            'prus': {'cmd': 0x89, 'func': to_byte_format},
            'prds': {'cmd': 0x8A, 'func': to_byte_format},
            'rcun1': {'cmd': 0xA3, 'func': to_comp28_format},
        },
        'read': {
            'rmv': {'cmd': 0xD0, 'func': from_comp28_format},
            'rfl': {'cmd': 0xD1, 'func': from_byte_format},
            'rfh': {'cmd': 0xD2, 'func': from_byte_format},
            'rur': {'cmd': 0xD3, 'func': from_byte_format},
            'rdr': {'cmd': 0xD4, 'func': from_byte_format},
            'rmg': {'cmd': 0xD5, 'func': from_byte_format},
            'rdp': {'cmd': 0xD6},
            'rmd': {'cmd': 0xD7},
            'rip': {'cmd': 0xD8},
            'rus': {'cmd': 0xD9},
            'rds': {'cmd': 0xDA},
            'renv1': {'cmd': 0x9C},
            'prmv': {'cmd': 0xC0, 'func': from_comp28_format},
            'prfl': {'cmd': 0xC1, 'func': from_byte_format},
            'prfh': {'cmd': 0xC2, 'func': from_byte_format},
            'prur': {'cmd': 0xC3, 'func': from_byte_format},
            'prdr': {'cmd': 0xC4, 'func': from_byte_format},
            'prmg': {'cmd': 0xC5, 'func': from_byte_format},
            'prdp': {'cmd': 0xC6},
            'prmd': {'cmd': 0xC7},
            'prip': {'cmd': 0xC8},
            'prus': {'cmd': 0xC9},
            'prds': {'cmd': 0xCA},
            'rcun1': {'cmd': 0xE3, 'func': from_comp28_format},
            'rcun2': {'cmd': 0xE4, 'func': from_comp28_format},
            'rcun3': {'cmd': 0xE5, 'func': from_comp16_format},
            'rcun4': {'cmd': 0xE6, 'func': from_comp28_format},
            'rltc1': {'cmd': 0xED, 'func': from_comp28_format},
            'rltc2': {'cmd': 0xEE, 'func': from_comp28_format},
            'rltc3': {'cmd': 0xEF, 'func': from_comp16_format},
            'rltc4': {'cmd': 0xF0, 'func': from_comp28_format},
            'rsts':  {'cmd': 0xF1, 'func': do_nothing},
            'rpls':  {'cmd': 0xF4, 'func': from_rpls_format},
            'rspd':  {'cmd': 0xF5, 'func': from_byte_format},
        },
        'send': {
            'fchgl': {'cmd': 0x40},
            'fchgh': {'cmd': 0x41},
            'fschl': {'cmd': 0x42},
            'fschh': {'cmd': 0x43},
            'stop': {'cmd': 0x49},
            'sdstp': {'cmd': 0x4a},
            'stafl': {'cmd': 0x50},
            'stafh': {'cmd': 0x51},
            'stad': {'cmd': 0x52},
            'staud': {'cmd': 0x53},
            'cntfl': {'cmd': 0x54},
            'cntfh': {'cmd': 0x55},
            'cntd': {'cmd': 0x56},
            'cntud': {'cmd': 0x57},
            'srst': {'cmd': 0x04},
        },
    }

    pulse_specific = {
        'pulse_dir1': 0x00,
        'pulse_dir2': 0x02,
        'pulse_dir3': 0x04,
        'pulse_dir4': 0x06,
        'two_pulse1': 0x01,
        'two_pulse2': 0x07,
        'phase_dif1': 0x03,
        'phase_dif2': 0x05,
        }

    move_mode = {
        'jog': 0x00,
        'org': None,
        'ptp': 0x42,
        'timer': None,
        'single_step': None,
        'org_search': None,
        'org_exit': None,
        'org_zero': None,
        'ptp_repeat': None,
    }

    _motion_conf_default = {
        'clock': 0,
        'acc_mode': '',
        'low_speed': 0,
        'speed': 0,
        'acc': 0,
        'dec': 0,
        'step': 0,
    }

    motion_conf = {
        'jog': {
            'x': _motion_conf_default.copy(),
            'y': _motion_conf_default.copy(),
            'z': _motion_conf_default.copy(),
            'u': _motion_conf_default.copy(),
        },
        'org': {
            'x': _motion_conf_default.copy(),
            'y': _motion_conf_default.copy(),
            'z': _motion_conf_default.copy(),
            'u': _motion_conf_default.copy(),
        },
        'ptp': {
            'x': _motion_conf_default.copy(),
            'y': _motion_conf_default.copy(),
            'z': _motion_conf_default.copy(),
            'u': _motion_conf_default.copy(),
        },
        'timer': {
            'x': _motion_conf_default.copy(),
            'y': _motion_conf_default.copy(),
            'z': _motion_conf_default.copy(),
            'u': _motion_conf_default.copy(),
        },
        'single_step': {
            'x': _motion_conf_default.copy(),
            'y': _motion_conf_default.copy(),
            'z': _motion_conf_default.copy(),
            'u': _motion_conf_default.copy(),
        },
        'org_search': {
            'x': _motion_conf_default.copy(),
            'y': _motion_conf_default.copy(),
            'z': _motion_conf_default.copy(),
            'u': _motion_conf_default.copy(),
        },
        'org_exit': {
            'x': _motion_conf_default.copy(),
            'y': _motion_conf_default.copy(),
            'z': _motion_conf_default.copy(),
            'u': _motion_conf_default.copy(),
        },
        'org_zero': {
            'x': _motion_conf_default.copy(),
            'y': _motion_conf_default.copy(),
            'z': _motion_conf_default.copy(),
            'u': _motion_conf_default.copy(),
        },
        'ptp_repeat': {
            'x': _motion_conf_default.copy(),
            'y': _motion_conf_default.copy(),
            'z': _motion_conf_default.copy(),
            'u': _motion_conf_default.copy(),
        },
    }

    _last_param = {}

    def get_board_id(self):
        bar = 0
        offset = 0x0F
        size = 1
        ret = self.read(bar, offset, size)
        bid = ret.to_hex()[1]
        return bid

    def _select_axis_for_command(self, axis):
        axis_num = 0b00000000
        axis_dict = {
            'x': 0b00000001,
            'y': 0b00000010,
            'z': 0b00000100,
            'u': 0b00001000,
        }
        for i in axis.lower():
            axis_num |= axis_dict[i]
        return axis_num

    def _make_offset_list(self, offset, axis):
        axis_dict = {'x': 0x00, 'y': 0x08, 'z': 0x10, 'u': 0x18,}
        axis_list = [offset + axis_dict[i] for i in axis.lower()]
        return axis_list

    def _pcl_write_command(self, cmd, axis):
        bar = 1
        offset = 0x00
        axis_num = self._select_axis_for_command(axis)
        cmd = cmd.to_bytes(1, 'little')
        axis_num = axis_num.to_bytes(1, 'little')
        cmdaxis = cmd + axis_num
        self.write(bar, offset, cmdaxis)
        time.sleep(5e-07)
        return

    def _pcl_write_data(self, data, axis):
        bar = 1
        offset = 0x04
        offset_list = self._make_offset_list(offset, axis)
        [self.write(bar, _o, _d) for _o, _d in zip(offset_list, data)]
        return

    def _pcl_read_data(self, axis):
        bar = 1
        offset = 0x04
        size = 4
        offset_list = self._make_offset_list(offset, axis)
        data_list = [self.read(bar, _o, size) for _o in offset_list]
        return data_list

    def _check_last_param(self, data, name, axis):
        if name in self._last_param:
            pass
        else:
            self._last_param[name] = {
                'x': None,
                'y': None,
                'z': None,
                'u': None,
            }
        _d = []
        _ax = ''
        for i, j in zip(data, axis):
            if i != self._last_param[name][j]:
                _d.append(i)
                _ax += j
                self._last_param[name][j] = i
        ret = [_d, _ax]
        return ret

    def set_param(self, data, name, axis):
        data_axis_list = self._check_last_param(data, name, axis)
        data = data_axis_list[0]
        axis = data_axis_list[1]
        if data != []:
            comb0 = self.cmd_dict['write'][name]['cmd']
            data = self.cmd_dict['write'][name]['func'](data)
            self._pcl_write_data(data, axis)
            self._pcl_write_command(comb0, axis)
        else: pass
        return

    def get_param(self, name, axis):
        comb0 = self.cmd_dict['read'][name]['cmd']
        self._pcl_write_command(comb0, axis)
        data_flag = self._pcl_read_data(axis)
        data = self.cmd_dict['read'][name]['func'](data_flag)
        return data

    def send_cmd(self, name, axis):
        comb0 = self.cmd_dict['send'][name]['cmd']
        self._pcl_write_command(comb0, axis)
        return

    def get_main_status(self, axis):
        bar = 1
        offset = 0x00
        size = 2
        offset_list = self._make_offset_list(offset, axis)
        status_list = []
        for i in offset_list:
            status_list.append(self.read(bar, i, size).to_bit())
            time.sleep(0.01)
        return status_list

    def check_move_onoff(self, axis):
        status_list = self.get_main_status(axis=axis)
        move_onoff_list = [int(i[0]) for i in status_list]
        return move_onoff_list

    def get_operate_condition(self, axis):
        data = self._get_extended_status(axis)
        data = [i[0:4][::-1] for i in data]
        return data

    def _get_onoff_axis(self, axis, onoff):
        _onoff = self.check_move_onoff(axis=axis)
        onoff_axis = ''
        for i, j in zip(_onoff, axis):
            if i == onoff:
                onoff_axis += j
            else: pass
        return onoff_axis

    def _get_extended_status(self, axis):
        data = self.get_param(name='rsts', axis=axis)
        data = [i.to_bit() for i in data]
        return data


    ###=== for gpg7400 ===###

    def initialize(self, axis='xyzu'):
        self.send_cmd(name='srst', axis=axis)
        time.sleep(0.1)
        return


    def reset(self, axis, mode):
        if mode == 'reset_ctrl':
            self.send_cmd(name='stop', axis='xyzu')
            self.send_cmd(name='srst', axis='xyzu')
        elif mode == 'reset_motion':
            self.send_cmd(name='stop', axis='xyzu')
            for i in self.motion_conf.values():
                for j in i: i[j] = _motion_conf_default.copy()

            data = [0]*len(axis)
            self.set_param(data=data, name='prmv', axis=axis)
            self.set_param(data=data, name='prfl', axis=axis)
            self.set_param(data=data, name='prfh', axis=axis)
            self.set_param(data=data, name='prur', axis=axis)
            self.set_param(data=data, name='prdr', axis=axis)
            self.set_param(data=data, name='prmg', axis=axis)

        else: pass
        return


    def set_pulse_out(self, axis, mode, config):
        renv1 = []
        if mode == 'method':
            for i, j in zip(axis, config):
                _con = j['DUTY'] + j['WAIT'] + j['DIR'] + j['OUT'] + j['PULSE']
                renv1.append(int(_con, 2))
            else: pass

        self.set_param(renv1, 'renv1', axis)
        return


    def set_motion(self, axis, mode, motion):
        for i in axis:
            self.motion_conf[mode][i] = motion[i].copy()
        return


    def get_motion(self, axis, mode):
        motion = {i: self.motion_conf[mode][i].copy() for i in axis}
        return motion


    def start_motion(self, axis, start_mode, move_mode):
        prmd = []
        for i in axis:
            if self.motion_conf[move_mode][i]['acc_mode'] == 'acc_normal':
                prmd.append(self.move_mode[move_mode])
            elif self.motion_conf[move_mode][i]['acc_mode'] == 'acc_sin':
                prmd.append(self.move_mode[move_mode]|0x04)
            else: pass

        self.set_param(prmd, 'prmd', axis)
        conf = self.motion_conf[move_mode]
        self.set_param([conf[i]['clock'] for i in axis], 'prmg', axis)
        self.set_param([conf[i]['low_speed'] for i in axis], 'prfl', axis)
        self.set_param([conf[i]['speed'] for i in axis], 'prfh', axis)
        self.set_param([conf[i]['acc'] for i in axis], 'prur', axis)
        self.set_param([conf[i]['dec'] for i in axis], 'prdr', axis)
        self.set_param([conf[i]['step'] for i in axis], 'prmv', axis)

        if start_mode == 'acc': self.send_cmd(name='staud', axis=axis)
        elif start_mode == 'const': self.send_cmd(name='stafh', axis=axis)
        elif start_mode == 'const_dec': self.send_cmd(name='stad', axis=axis)
        else: pass
        return


    def stop_motion(self, axis, stop_mode):
        if stop_mode == 'dec_stop':
            self.send_cmd(name='sdstp', axis=axis)
        elif stop_mode == 'immediate_stop':
            self.send_cmd(name='stop', axis=axis)
        else: pass
        return


    def change_speed(self, axis, mode, speed):
        if mode == 'accdec_change':
            self.set_param(name='rfh', data=speed, axis=axis)
        else: pass
        return


    def change_step(self, axis, step):
        self.set_param(name='rmv', data=step, axis=axis)
        return


    def read_speed(self, axis):
        data = self.get_param(name='rspd', axis=axis)
        return data


    def read_counter(self, axis, cnt_mode):
        if cnt_mode == 'counter':
            data = self.get_param(name='rcun1', axis=axis)
        else: data = None
        return data


    def write_counter(self, axis, cnt_mode, counter):
        if cnt_mode == 'counter':
            self.set_param(name='rcun1', data=counter, axis=axis)
        else: pass
        return


    def output_do(self, do):
        bar = 0
        offset = 0x02
        do = do.to_bytes(2, 'little')
        self.write(bar, offset, do)
        return


    def input_di(self):
        bar = 0
        offset = 0x02
        size = 2
        data = self.read(bar, offset, size)
        return data.to_dictlist()
