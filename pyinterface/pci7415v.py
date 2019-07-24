
import struct
import time
from . import core

# functions
# =========

def to_comp28_format(x):
    data = []
    for i in range(len(x)):
        a = int(x[i]) & 0xfffffff
        data.append(struct.pack('<I', a))
    return data

def to_comp16_format(x):
    data = []
    for i in range(len(x)):
        a = int(x[i]) & 0xffff
        data.append(struct.pack('<I', a))
    return data

def to_byte_format(x):
    data = []
    for i in range(len(x)):
        a = x[i]
        data.append(struct.pack('<I', a))
    return data

def to_prmd_format(x):
    pass

def to_prip_format(x):
    data = []
    for i in range(len(x)):
        a = x[i] & 0xfffffff
        data.append(struct.pack('<I', a))
    return data

def from_comp28_format(x):
    data = []
    for i in range(len(x)):
        a = x[i].to_bit()
        b = a[0:28][::-1]
        c = -int(b[0]) << len(b) | int(b, 2)
        data.append(c)
    return data

def from_comp16_format(x):
    data = []
    for i in range(len(x)):
        a = x[i].to_bit()
        b = a[0:16][::-1]
        c = -int(b[0]) << len(b) | int(b, 2)
        data.append(c)
    return data

def from_byte_format(x):
    data = []
    for i in range(len(x)):
        a = x[i].to_int()
        data.append(a)
    return data

def from_rpls_format(x):
    data = []
    for i in range(len(x)):
        a = x[i].to_bit()
        b = a[0:28][::-1]
        c = -int(b[0]) << len(b) | int(b, 2)
        data.append(c)
    return data

def do_nothing(x):
    return x


class pci7415v_driver(core.interface_driver):
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

    cmd_dic = {
        'write': {
            'rmv':   {'cmd': 0x90, 'func': to_comp28_format},
            'rfl':   {'cmd': 0x91, 'func': to_byte_format},
            'rfh':   {'cmd': 0x92, 'func': to_byte_format},
            'rur':   {'cmd': 0x93, 'func': to_byte_format},
            'rdr':   {'cmd': 0x94, 'func': to_byte_format},
            'rmg':   {'cmd': 0x95, 'func': to_byte_format},
            'rdp':   {'cmd': 0x96, 'func': to_byte_format},
            'rmd':   {'cmd': 0x97, 'func': to_prmd_format},
            'rip':   {'cmd': 0x98, 'func': to_prip_format},
            'rus':   {'cmd': 0x99, 'func': to_byte_format},
            'rds':   {'cmd': 0x9A, 'func': to_byte_format},
            'prmv':  {'cmd': 0x80, 'func': to_comp28_format},
            'prfl':  {'cmd': 0x81, 'func': to_byte_format},
            'prfh':  {'cmd': 0x82, 'func': to_byte_format},
            'prur':  {'cmd': 0x83, 'func': to_byte_format},
            'prdr':  {'cmd': 0x84, 'func': to_byte_format},
            'prmg':  {'cmd': 0x85, 'func': to_byte_format},
            'prdp':  {'cmd': 0x86, 'func': to_byte_format},
            'prmd':  {'cmd': 0x87, 'func': to_byte_format},
            'prip':  {'cmd': 0x88, 'func': to_prip_format},
            'prus':  {'cmd': 0x89, 'func': to_byte_format},
            'prds':  {'cmd': 0x8A, 'func': to_byte_format},
            'rcun1': {'cmd': 0xA3, 'func': to_comp28_format}
        },
        'read': {
            'rmv':   {'cmd': 0xD0, 'func': from_comp28_format},
            'rfl':   {'cmd': 0xD1, 'func': from_byte_format},
            'rfh':   {'cmd': 0xD2, 'func': from_byte_format},
            'rur':   {'cmd': 0xD3, 'func': from_byte_format},
            'rdr':   {'cmd': 0xD4, 'func': from_byte_format},
            'rmg':   {'cmd': 0xD5, 'func': from_byte_format},
            'rdp':   {'cmd': 0xD6},
            'rmd':   {'cmd': 0xD7},
            'rip':   {'cmd': 0xD8},
            'rus':   {'cmd': 0xD9},
            'rds':   {'cmd': 0xDA},
            'prmv':  {'cmd': 0xC0, 'func': from_comp28_format},
            'prfl':  {'cmd': 0xC1, 'func': from_byte_format},
            'prfh':  {'cmd': 0xC2, 'func': from_byte_format},
            'prur':  {'cmd': 0xC3, 'func': from_byte_format},
            'prdr':  {'cmd': 0xC4, 'func': from_byte_format},
            'prmg':  {'cmd': 0xC5, 'func': from_byte_format},
            'prdp':  {'cmd': 0xC6},
            'prmd':  {'cmd': 0xC7},
            'prip':  {'cmd': 0xC8},
            'prus':  {'cmd': 0xC9},
            'prds':  {'cmd': 0xCA},
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
            'rspd':  {'cmd': 0xF5, 'func': from_byte_format}
        },
        'send': {
            'fchgl': {'cmd': 0x40}, 'fchgh': {'cmd': 0x41},
            'fschl': {'cmd': 0x42}, 'fschh': {'cmd': 0x43},
            'stop':  {'cmd': 0x49}, 'sdstp': {'cmd': 0x4a},
            'stafl': {'cmd': 0x50}, 'stafh': {'cmd': 0x51},
            'stad':  {'cmd': 0x52}, 'staud': {'cmd': 0x53},
            'cntfl': {'cmd': 0x54}, 'cntfh': {'cmd': 0x55},
            'cntd':  {'cmd': 0x56}, 'cntud': {'cmd': 0x57},
            'srst':  {'cmd': 0x04}
        }
    }

    move_mode = {
        'jog': 0x00, 'org': None, 'ptp': 0x42,
        'timer': None, 'single_step': None, 'org_search': None,
        'org_exit': None, 'org_zero': None, 'ptp_repeat': None
    }

    motion_conf = {
        'jog': {
            'x': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'y': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'z': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'u': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            }
        },
        'org': {
            'x': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'y': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'z': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'u': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            }
        },
        'ptp': {
            'x': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'y': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'z': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'u': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            }
        },
        'timer': {
            'x': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'y': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'z': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'u': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            }
        },
        'single_step': {
            'x': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'y': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'z': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'u': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            }
        },
        'org_search': {
            'x': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'y': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'z': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'u': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            }
        },
        'org_exit': {
            'x': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'y': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'z': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'u': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            }
        },
        'org_zero': {
            'x': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'y': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'z': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'u': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            }
        },
        'ptp_repeat': {
            'x': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'y': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'z': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            },
            'u': {
                'clock':  0, 'acc_mode': '', 'low_speed': 0,
                'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
            }
        }
    }


    def get_board_id(self):
        bar = 0
        offset = 0x0F
        size = 1
        ret = self.read(bar, offset, size)
        bid = ret.to_hex()[1]
        return bid

    def _select_axis_for_command(self, axis):
        axis_num = 0b00000000
        axis_dic = {'x': 0b00000001, 'X': 0b00000001,
                    'y': 0b00000010, 'Y': 0b00000010,
                    'z': 0b00000100, 'Z': 0b00000100,
                    'u': 0b00001000, 'U': 0b00001000}
        for i in range(len(axis)):
            axis_num |= axis_dic[axis[i]]
        return axis_num

    def _make_offset_list(self, offset, axis):
        axis_dic = {'x': 0x00, 'y': 0x08, 'z': 0x10, 'u': 0x18,
                    'X': 0x00, 'Y': 0x08, 'Z': 0x10, 'U': 0x18}
        axis_li = []
        for i in range(len(axis)):
            axis_li.append(offset + axis_dic[axis[i]])
        return axis_li

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
        offset_li = self._make_offset_list(offset, axis)
        for i in range(len(axis)):
            self.write(bar, offset_li[i], data[i])
        return

    def _pcl_read_data(self, axis):
        bar = 1
        offset = 0x04
        offset_li = self._make_offset_list(offset, axis)
        size = 4
        data_li = []
        for i in range(len(axis)):
            data_li.append(self.read(bar, offset_li[i], size))
        return data_li

    def set_param(self, data, name, axis):
        comb0 = self.cmd_dic['write'][name]['cmd']
        data = self.cmd_dic['write'][name]['func'](data)
        self._pcl_write_data(data, axis)
        self._pcl_write_command(comb0, axis)
        return

    def get_param(self, name, axis):
        comb0 = self.cmd_dic['read'][name]['cmd']
        self._pcl_write_command(comb0, axis)
        data_flag = self._pcl_read_data(axis)
        data = self.cmd_dic['read'][name]['func'](data_flag)
        return data

    def send_cmd(self, name, axis):
        comb0 = self.cmd_dic['send'][name]['cmd']
        self._pcl_write_command(comb0, axis)
        return

    def get_main_status(self, axis):
        bar = 1
        offset = 0x00
        offset_li = self._make_offset_list(offset, axis)
        size = 2
        status_li = []
        for i in range(len(axis)):
            status = self.read(bar, offset_li[i], size)
            status_li.append(status.to_bit())
            time.sleep(0.01)
        return status_li

    def check_move_onoff(self, axis):
        status_li = self.get_main_status(axis=axis)
        move_onoff_list = []
        for i in range(len(axis)):
            move_onoff_list.append(int(status_li[i][0]))
        return move_onoff_list

    def get_operate_condition(self, axis):
        data = self._get_extended_status(axis)
        for i in range(len(data)):
            data[i] = data[i][0:4][::-1]
        return data

    def _get_onoff_axis(self, axis, onoff):
        _onoff = self.check_move_onoff(axis=axis)
        onoff_axis = ''
        for i in range(len(axis)):
            if _onoff[i] == onoff: onoff_axis = onoff_axis + axis[i]
            else: pass
        return onoff_axis

    def _get_extended_status(self, axis):
        data = self.get_param(name='rsts', axis=axis)
        for i in range(len(axis)):
            data[i] = data[i].to_bit()
        return data

    def _dict2list(self, axis, move_mode, param):
        data_li = []
        [data_li.append(self.motion_conf[move_mode][i][param]) for i in axis]
        return data_li

    def _list2dict(self, axis, data_li):
        data_dic = {}
        j = 0
        for i in axis:
            data_dic[i] = data_li[j]
            j += 1
        return data_dic


    ###=== for gpg7400 ===###


    def initialize(self, axis='xyzu'):
        self.send_cmd(name='srst', axis=axis)
        time.sleep(0.1)
        return


    def reset(self, axis, mode):
        if mode == 'reset_ctrl':
            self.send_cmd(name='stop', axis='xyzu')
            self.send_cmd(name='srst', axis='xyzu')
        if mode == 'reset_motion':
            self.send_cmd(name='stop', axis='xyzu')
            for i in self.motion_conf:
                for j in self.motion_conf[i]:
                    self.motion_conf[i][j] = {
                        'clock':  0, 'acc_mode': '', 'low_speed': 0,
                        'speed': 0, 'acc': 0, 'dec': 0, 'step': 0
                    }
            data = [0]*len(axis)
            self.set_param(data=data, name='prmv', axis=axis)
            self.set_param(data=data, name='prfl', axis=axis)
            self.set_param(data=data, name='prfh', axis=axis)
            self.set_param(data=data, name='prur', axis=axis)
            self.set_param(data=data, name='prdr', axis=axis)
            self.set_param(data=data, name='prmg', axis=axis)
            return


    def set_motion(self, axis, mode, motion):
        for i in axis:
            for j in motion[i]:
                self.motion_conf[mode][i][j] = motion[i][j]
        return


    def get_motion(self, axis, mode):
        motion = {}
        for i in axis:
            motion[i] = self.motion_conf[mode][i]
        return motion


    def start_motion(self, axis, start_mode, move_mode):
        prmd = []
        for i in axis:
            if self.motion_conf[move_mode][i]['acc_mode'] == 'acc_normal':
                prmd.append(self.move_mode[move_mode])
            if self.motion_conf[move_mode][i]['acc_mode'] == 'acc_sin':
                prmd.append(self.move_mode[move_mode]|0x04)
        self._start_motion(axis=axis, prmd=prmd, move_mode=move_mode)
        if start_mode == 'acc': self.send_cmd(name='staud', axis=axis)
        if start_mode == 'const': self.send_cmd(name='stafh', axis=axis)
        if start_mode == 'const_dec': self.send_cmd(name='stad', axis=axis)
        return


    def _start_motion(self, axis, prmd, move_mode):
        self.set_param(self._dict2list(axis, move_mode, 'clock'), 'rmg', axis)
        self.set_param(prmd, 'prmd', axis)
        self.set_param(self._dict2list(axis, move_mode, 'low_speed'), 'rfl', axis)
        self.set_param(self._dict2list(axis, move_mode, 'speed'), 'rfh', axis)
        self.set_param(self._dict2list(axis, move_mode, 'acc'), 'rur', axis)
        self.set_param(self._dict2list(axis, move_mode, 'dec'), 'rdr', axis)
        self.set_param(self._dict2list(axis, move_mode, 'step'), 'rmv', axis)
        return


    def stop_motion(self, axis, stop_mode):
        if stop_mode == 'dec_stop':
            self.send_cmd(name='sdstp', axis=axis)
        if stop_mode == 'immediate_stop':
            self.send_cmd(name='stop', axis=axis)
        return


    def change_speed(self, axis, mode, speed):
        if mode == 'accdec_change':
            self.set_param(name='rfh', data=speed, axis=axis)
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
        return data


    def write_counter(self, axis, cnt_mode, counter):
        if cnt_mode == 'counter':
            self.set_param(name='rcun1', data=counter, axis=axis)
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
