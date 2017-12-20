
import pypci

from . import pci2702
from . import pci2724
from . import pci6204
from . import pci7204


interface_vendor_id = 0x1147


def open(board_name, board_id):    
    if type(board_id) == int:
        board_id = format(board_id, '1X')
        pass
    
    board_list = pypci.lspci(interface_vendor_id, board_name)
    
    if board_list == []:
        msg = 'board_id {0} is not found'.format(board_name)
        raise TypeError(msg)
    
    for board in board_list:
        if board_name == 2702:
            b = pci2702.pci2702_driver(board)
            if b.board_id == board_id:
                return b
            pass
        
        if board_name == 2724:
            b = pci2724.pci2724_driver(board)
            if b.board_id == board_id:
                return b
            pass
        
        if board_name == 6204:
            b = pci6204.pci6204_driver(board)
            if b.board_id == board_id:
                return b
            pass


        if board_name == 7204:
            b = pci7204.pci7204_driver(board)
            if b.board_id == board_id:
                return b
            pass

        continue
    
