# Interface PCI board driver for python

## Environment
- Linux
- python 3
- require : [portio module](http://portio.inrim.it/)


## Installation
`pip install pyinterface`


## Usage

    import pyinterface
    
    board_name = 2704
    rsw_id = 2
    
    b = pyinterface.open(board_name, rsw_id)
    b.input_byte('IN1_8')
    >>> [0, 0, 0, 0, 0, 0, 0, 0]
    
    b.output_byte([0, 1, 0, 1, 0, 0, 1, 1], 'OUT25_32')
    >>> 000000CA

