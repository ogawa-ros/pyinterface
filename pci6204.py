
from .core import interface_driver
from .core import Bytes

# exceptions
# ----------
class InvalidChannelError(Exception):
    def __init__(self, message):
        self.message = message
        pass



class pci6204_in0(Bytes):
    data = [
        {'name': ['CD0', 'CD1', 'CD2', 'CD3', 'CD4', 'CD5', 'CD6', 'CD7']},
        {'name': ['CD8', 'CD9', 'CD10', 'CD11', 'CD12', 'CD13', 'CD14', 'CD15']},
        {'name': ['CD16', 'CD17', 'CD18', 'CD19', 'CD20', 'CD21', 'CD22', 'CD23']},
        {'name': ['CD24', 'CD25', 'CD26', 'CD27', 'CD28', 'CD29', 'CD30', 'CD31']},
        {'name': ['SEL0', 'SEL1', 'MD0', 'MD1', 'DIR', 'EQS', '', '']},
        {'name': ['A', 'B', 'Z', 'L1', 'L2', 'L3', '', '']},
        {'name': ['U/D', 'CBF', 'EQ', 'EXLTS', 'EQF', 'PERR', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', '']},
        {'name': ['L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['CD0', 'CD1', 'CD2', 'CD3', 'CD4', 'CD5', 'CD6', 'CD7']},
        {'name': ['CD8', 'CD9', 'CD10', 'CD11', 'CD12', 'CD13', 'CD14', 'CD15']},
        {'name': ['CD16', 'CD17', 'CD18', 'CD19', 'CD20', 'CD21', 'CD22', 'CD23']},
        {'name': ['CD24', 'CD25', 'CD26', 'CD27', 'CD28', 'CD29', 'CD30', 'CD31']},
        {'name': ['SEL0', 'SEL1', 'MD0', 'MD1', 'DIR', 'EQS', '', '']},
        {'name': ['A', 'B', 'Z', 'L1', 'L2', 'L3', '', '']},
        {'name': ['U/D', 'CBF', 'EQ', 'EXLTS', 'EQF', 'PERR', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', '']},
        {'name': ['L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
    ]

class pci6204_out0(Bytes):
    data = [
        {'name': ['WD0', 'WD1', 'WD2', 'WD3', 'WD4', 'WD5', 'WD6', 'WD7']},
        {'name': ['WD8', 'WD9', 'WD10', 'WD11', 'WD12', 'WD13', 'WD14', 'WD15']},
        {'name': ['WD16', 'WD17', 'WD18', 'WD19', 'WD20', 'WD21', 'WD22', 'WD23']},
        {'name': ['WD24', 'WD25', 'WD26', 'WD27', 'WD28', 'WD29', 'WD30', 'WD31']},
        {'name': ['SEL0', 'SEL1', 'MD0', 'MD1', 'DIR', 'EQS', '', '']},
        {'name': ['P/L', '/EN', '', '', '', '', '', '']},
        {'name': ['CC0', 'CC1', '', '', '', '', '', '']},
        {'name': ['CLS0', 'CLS1', 'LTS0', 'LTS1', 'ZP', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['WD0', 'WD1', 'WD2', 'WD3', 'WD4', 'WD5', 'WD6', 'WD7']},
        {'name': ['WD8', 'WD9', 'WD10', 'WD11', 'WD12', 'WD13', 'WD14', 'WD15']},
        {'name': ['WD16', 'WD17', 'WD18', 'WD19', 'WD20', 'WD21', 'WD22', 'WD23']},
        {'name': ['WD24', 'WD25', 'WD26', 'WD27', 'WD28', 'WD29', 'WD30', 'WD31']},
        {'name': ['SEL0', 'SEL1', 'MD0', 'MD1', 'DIR', 'EQS', '', '']},
        {'name': ['P/L', '/EN', '', '', '', '', '', '']},
        {'name': ['CC0', 'CC1', '', '', '', '', '', '']},
        {'name': ['CLS0', 'CLS1', 'LTS0', 'LTS1', 'ZP', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
    ]

class pci6204_in1(Bytes):
    data = [
        {'name': ['TD1', 'TD2', 'TD3', 'TD4', '', '', '', '']},
        {'name': ['', '', '', '', 'SIGT', '', '', '']},
        {'name': ['', '', '', '', 'SIGT', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['BID0', 'BID1', 'BID2', 'BID3', '', '', '', '']},
    ]

class pci6204_out1(Bytes):
    data = [
        {'name': ['TCTRL1', 'TCTRL2', 'TCTRL3', 'TCTRL4', 'SCK1', 'SCK2', 'SCK3', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', 'SIGT', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
        {'name': ['', '', '', '', '', '', '', '']},
    ]

class pci6204_driver(interface_driver):
    def __init__(self, config):
        self.bytes_in = [pci6204_in0(addr=config.port[0].addr),
                         pci6204_in1(addr=config.port[1].addr)]
        self.bytes_out = [pci6204_out0(addr=config.port[0].addr),
                          pci6204_out1(addr=config.port[1].addr)]
        super().__init__(config)
        pass
    
    def _get_board_id(self):
        return self.read(self.bytes_in[1][0x0f])
    
    def _get_address_for(self, ch, base_addr):
        offset = {1: 0x00, 2: 0x10}
        
        if ch not in offset:
            raise InvalidChannelError('ch should be 1 or 2 while {0} is given.'.format(ch))

        return base_addr + offset[ch]
    
    def _get_register_for(self, ch, base_addr, size=1):
        addr = self._get_address_for(ch, base_addr)
        target = self.bytes_in[0][addr:addr+size]
        return self.read(target)
    
    def _set_register_for(self, ch, base_addr, data, size=1):
        addr = self._get_address_for(ch, base_addr)
        target = self.bytes_out[0][addr:addr+size]
        target.set(data)
        return self.write(target)

    def _get_out_chache_for(self, ch, base_addr):
        addr = self._get_address_for(ch, base_addr)
        target = self.bytes_out[0][addr]
        return target

    def _write_to_counter(self, ch):
        addr = 0x05
        flags = ''
        b = self._get_out_chache_for(ch, addr)
        flags += ' /EN' if (b['/EN'] == 1) else ''
        return self._set_register_for(ch, addr, flags)
    
    def _write_to_comparator(self, ch):
        addr = 0x05
        flags = 'P/L'
        b = self._get_out_chache_for(ch, addr)
        flags += ' /EN' if (b['/EN'] == 1) else ''
        return self._set_register_for(ch, addr, flags)
    
    def _latch(self, ch):
        base_addr = 0x06
        flags = 'CC1'
        return self._set_register_for(ch, base_addr, flags)
    
    def initialize(self):
        self.bytes_in[0].set(0)
        self.bytes_in[1].set(0)
        self.bytes_out[0].set(0)
        self.bytes_out[1].set(0)
        self.set_counter(0x00000000, ch=1)
        self.set_counter(0x00000000, ch=2)
        self.set_comparator(0xffffffff, ch=1)
        self.set_comparator(0xffffffff, ch=2)
        self.set_mode(ch=1)
        self.set_mode(ch=2)
        self.enable_count(ch=1)
        self.enable_count(ch=2)
        self._write_to_counter(ch=1)
        self._write_to_counter(ch=2)
        self.set_z_mode(ch=1)
        self.set_z_mode(ch=2)
        pass
    
    def reset(self, ch=1):
        """Reset count value for specified ch.
        Compatibility: PencReset function in GPG-6204 driver
        
        Parameters
        ----------
        ch : int (1:default or 2)
            Target channel number.
        """
        base_addr = 0x06
        flags = 'CC0 CC1'
        return self._set_register_for(ch, base_addr, flags)
    
    def set_mode(self, mode='', direction=0, equal=0, latch=0, ch=1):
        """Configure count mode, direction, equal detection and latch mode.
        Compatibility: PencSetMode function in GPG-6204 driver
        
        Parameters
        ----------
        mode : str ('SEL0', 'SEL1', 'MD0' and/or 'MD1')
            pulse count mode
            ''     = Single pulse, x1
            'SEL0' = Single pulse, x2
            'MD0'      = A/B phase, x1, async
            'MD0 SEL0' = A/B phase, x2, async
            'MD0 SEL1' = A/B phase, x4, async
            'MD0 MD1'      = A/B phase, x1, sync
            'MD0 MD1 SEL0' = A/B phase, x2, sync
            'MD0 MD1 SEL1' = A/B phase, x4, sync
            'MD1'  = CW/CCW pulse
        
        direction : int (0 or 1)
            pulse count direction
            0 = Up
            1 = Down
        
        equal : int (0 or 1)
            enable/disable equal detection
            0 = disable
            1 = enable
        
        latch : int (0 or 1)
            latch mode
            0 : use software latch
            1 : use outer latch
        
        ch : int (1:default or 2)
            Target channel number.
        """
        base_addr = 0x04
        flags = mode
        if direction == 1: flags += ' DIR'
        if equal == 1: flags += ' EQS'
        return self._set_register_for(ch, base_addr, flags)
    
    def get_mode(self, ch=1):
        """Get count mode, direction, equal detection and latch mode.
        Compatibility: PencGetMode function in GPG-6204 driver
        
        Parameters
        ----------
        ch : int (1:default or 2)
            Target channel number.
        
        Returns
        -------
        pyinterface.Bytes object
            This object containes flags of SEL0, SEL1, MD0, MD1, DIR and EQS.
            To check the flags, call print() method of returned object.
            ex) b = pci6204.get_mode()
                b.print()
            
            SEL0, SEL1, MD0, MD1 flags represent pulse count mode:
                ''     = Single pulse, x1
                'SEL0' = Single pulse, x2
                'MD0'      = A/B phase, x1, async
                'MD0 SEL0' = A/B phase, x2, async
                'MD0 SEL1' = A/B phase, x4, async
                'MD0 MD1'      = A/B phase, x1, sync
                'MD0 MD1 SEL0' = A/B phase, x2, sync
                'MD0 MD1 SEL1' = A/B phase, x4, sync
                'MD1'  = CW/CCW pulse
            
            DIR flag represents pulse count direction:
                0 = Up
                1 = Down
            
            EQS flag represents enable/disable status of equal detection:
                0 = disable
                1 = enable
        """
        base_addr = 0x04
        return self._get_register_for(ch, base_addr)
    
    def set_z_mode(self, clear_condition='', latch_condition='', z_polarity=0, ch=1):
        """Configure clear condition, latch condition and Z polarity.
        Compatibility: PencSetZMode function in GPG-6204 driver
        
        Parameters
        ----------
        clear_condition : str ('CLS0' or 'CLS1')
            counter clear condition:
            ''     = disable
            'CLS0' = clear when Z phase is detected
            'CLS1' = clear when Z phase and latch signal are detected
        
        latch_condition : str ('LTS0' or 'LTS1')
            latch condition:
            ''     = disable
            'LTS0' = latch when latch signal is detected
            'LTS1' = latch when latch signal and Z phase are detected
        
        z_polarity : int (0 or 1)
            specify polarity for Z phase
            0 = normal (High)
            1 = inverse (Low)
        
        ch : int (1:default or 2)
            Target channel number.
        """
        base_addr = 0x07
        flags = ' '.join([clear_condition, latch_condition])
        if z_polarity == 1: flags += ' ZP'
        return self._set_register_for(ch, base_addr, flags)

    def get_z_mode(self, ch=1):
        """
        Compatibility: PencGetZMode function in GPG-6204 driver
        """
        base_addr = 0x07
        return self._get_out_chache_for(ch, base_addr)

    def enable_count(self, ch=1):
        """
        Compatibility: PencEnableCount function in GPG-6204 driver
        """
        base_addr = 0x05
        flags = ''
        return self._set_register_for(ch, base_addr, flags)

    def disable_count(self, ch=1):
        """
        Compatibility: PencEnableCount function in GPG-6204 driver
        """
        base_addr = 0x05
        flags = '/EN'
        return self._set_register_for(ch, base_addr, flags)
    
    def set_counter(self, count, ch=1):
        """
        Compatibility: PencSetCounter function in GPG-6204 driver
        """
        base_addr = 0x00
        size = 4
        data = count
        self._write_to_counter(ch)
        return self._set_register_for(ch, base_addr, data, size)
    
    def get_counter(self, ch=1):
        """
        Compatibility: PencGetCounter function in GPG-6204 driver
        """
        base_addr = 0x00
        size = 4
        self._latch(ch)
        return self._get_register_for(ch, base_addr, size)
    
    def set_comparator(self, count, ch=1):
        """
        Compatibility: PencSetComparator function in GPG-6204 driver
        """
        base_addr = 0x00
        size = 4
        data = count
        self._write_to_comparator(ch)
        return self._set_register_for(ch, base_addr, data, size)
    
    def get_status(self, ch=1):
        """
        Compatibility: PencGetStatus function in GPG-6204 driver
        """
        base_addr = 0x05
        size = 2
        return self._get_register_for(ch, base_addr, size)
    
    
    


    
