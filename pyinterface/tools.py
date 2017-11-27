
import os
import subprocess
import portio

from . import core
from . import pci2724
from . import pci6204

iopl_flag = False


def acquire_io_access_permission():
    global iopl_flag
    
    # root privilege is required
    if os.getuid() != 0: # uid = 0 : root
        raise Exception('root privilege is required to run pyinterface module')
    
    ret = portio.iopl(3)
    if ret == 0:
        iopl_flag = True
        print('INFO: I/O access is available (using root privileges)')
        pass
    return ret

def find_interface_board():
    # data acquisition
    # ----------------
    # human readable
    cmd1 = ['lspci', '-d', '1147:', '-v', '-nn']
    res1 = subprocess.run(cmd1, stdout=subprocess.PIPE)
    msg1 = res1.stdout.decode('utf-8').split('\n\n')
    
    # machine readable
    cmd2 = ['lspci', '-d', '1147:', '-v', '-mm', '-n']
    res2 = subprocess.run(cmd2, stdout=subprocess.PIPE)
    msg2 = res2.stdout.decode('utf-8').split('\n\n')
    
    # memory dump
    cmd3 = ['lspci', '-d', '1147:', '-xxxx']
    res3 = subprocess.run(cmd3, stdout=subprocess.PIPE)
    msg3 = res3.stdout.decode('utf-8').split('\n\n')
    
    # make data dictionary
    # --------------------
    ret = []
    for m1, m2, m3 in zip(msg1, msg2, msg3):
        if (m1 == '') or (m2 == '') or (m3 == ''): continue
        
        d = {}

        # parse machine readable output
        for line in m2.split('\n'):
            if line=='': continue
            key, value = line.split(':\t')
            if key != 'Slot':
                value = int(value, 16)
            if key == 'Class': key = 'device_class'
            d[key.lower()] = value
            continue

        # parse human readable output to get I/O port addr
        d_io = []
        for line in m1.split('\n'):
            line = line.strip('\t')
            if line.startswith('I/O ports at'):
                io_addr_str = line.split(' at ')[1].split(' [')[0]
                io_addr = int(io_addr_str, 16)
                io_size_str = line.split('[size=')[1].split(']')[0]                
                io_size = int(io_size_str)
                port_info = core.PortInfo(addr = io_addr,
                                          addr16 = io_addr_str,
                                          size = io_size)
                d_io.append(port_info)
                continue
            continue
        d['port'] = d_io
        d['text'] = m1

        # parse memory dump
        dump_text = '\n'.join(m3.split('\n')[1:])

        d_dump = b''
        for line in dump_text.split('\n'):
            line = line.split(': ')[1]
            for byte in line.split(' '):
                d_dump += int(byte, 16).to_bytes(1, 'little')
                continue
            continue
        d['dump'] = d_dump

        board_info = core.BoardInfo(**d)        
        ret.append(board_info)
        continue
    
    return ret


def open(board_name, board_id):
    if not iopl_flag:
        acquire_io_access_permission()
        pass
    
    board_list = find_interface_board()
    
    for board in board_list:
        if board.device == board_name == 2724:
            b = pci2724.pci2724_driver(board)
            if b.bid == board_id:
                return b
            pass
        
        if board.device == board_name == 6204:
            b = pci6204.pci6204_driver(board)
            if b.bid == board_id:
                return b
            pass
        continue
    
