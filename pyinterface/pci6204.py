
import struct
from . import core


class InvalidChannelError(Exception):
    pass


class pci6204_driver(core.interface_driver):
    bit_flags_in = (
        (
            ('CD0', 'CD1', 'CD2', 'CD3', 'CD4', 'CD5', 'CD6', 'CD7'),
            ('CD8', 'CD9', 'CD10', 'CD11', 'CD12', 'CD13', 'CD14', 'CD15'),
            ('CD16', 'CD17', 'CD18', 'CD19', 'CD20', 'CD21', 'CD22', 'CD23'),
            ('CD24', 'CD25', 'CD26', 'CD27', 'CD28', 'CD29', 'CD30', 'CD31'),
            ('SEL0', 'SEL1', 'MD0', 'MD1', 'DIR', 'EQS', '', ''),
            ('A', 'B', 'Z', 'L1', 'L2', 'L3', '', ''),
            ('U/D', 'CBF', 'EQ', 'EXLTS', 'EQF', 'PERR', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', ''),
            ('L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('CD0', 'CD1', 'CD2', 'CD3', 'CD4', 'CD5', 'CD6', 'CD7'),
            ('CD8', 'CD9', 'CD10', 'CD11', 'CD12', 'CD13', 'CD14', 'CD15'),
            ('CD16', 'CD17', 'CD18', 'CD19', 'CD20', 'CD21', 'CD22', 'CD23'),
            ('CD24', 'CD25', 'CD26', 'CD27', 'CD28', 'CD29', 'CD30', 'CD31'),
            ('SEL0', 'SEL1', 'MD0', 'MD1', 'DIR', 'EQS', '', ''),
            ('A', 'B', 'Z', 'L1', 'L2', 'L3', '', ''),
            ('U/D', 'CBF', 'EQ', 'EXLTS', 'EQF', 'PERR', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', ''),
            ('L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
        ),
        (
            ('TD1', 'TD2', 'TD3', 'TD4', '', '', '', ''),
            ('', '', '', '', 'SIGT', '', '', ''),
            ('', '', '', '', 'SIGT', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('BID0', 'BID1', 'BID2', 'BID3', '', '', '', ''),
        )
    )
     
    bit_flags_out = (
        (
            ('WD0', 'WD1', 'WD2', 'WD3', 'WD4', 'WD5', 'WD6', 'WD7'),
            ('WD8', 'WD9', 'WD10', 'WD11', 'WD12', 'WD13', 'WD14', 'WD15'),
            ('WD16', 'WD17', 'WD18', 'WD19', 'WD20', 'WD21', 'WD22', 'WD23'),
            ('WD24', 'WD25', 'WD26', 'WD27', 'WD28', 'WD29', 'WD30', 'WD31'),
            ('SEL0', 'SEL1', 'MD0', 'MD1', 'DIR', 'EQS', '', ''),
            ('P/L', '/EN', '', '', '', '', '', ''),
            ('CC0', 'CC1', '', '', '', '', '', ''),
            ('CLS0', 'CLS1', 'LTS0', 'LTS1', 'ZP', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('WD0', 'WD1', 'WD2', 'WD3', 'WD4', 'WD5', 'WD6', 'WD7'),
            ('WD8', 'WD9', 'WD10', 'WD11', 'WD12', 'WD13', 'WD14', 'WD15'),
            ('WD16', 'WD17', 'WD18', 'WD19', 'WD20', 'WD21', 'WD22', 'WD23'),
            ('WD24', 'WD25', 'WD26', 'WD27', 'WD28', 'WD29', 'WD30', 'WD31'),
            ('SEL0', 'SEL1', 'MD0', 'MD1', 'DIR', 'EQS', '', ''),
            ('P/L', '/EN', '', '', '', '', '', ''),
            ('CC0', 'CC1', '', '', '', '', '', ''),
            ('CLS0', 'CLS1', 'LTS0', 'LTS1', 'ZP', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('L2', 'L3', 'EQ', 'EXLT', 'C/B', 'PERR', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
        ),
        (
            ('TCTRL1', 'TCTRL2', 'TCTRL3', 'TCTRL4', 'SCK1', 'SCK2', 'SCK3', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', 'SIGT', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
        )
    )
    
    
    def get_board_id(self):
        bar = 1
        offset = 0x0f
        size = 1
        
        ret = self.read(bar, offset, size)
        bid = ret.to_hex()[1]
        return bid
    
    
    def initialize(self):
        self.set_counter(0, ch=1)
        self.set_counter(0, ch=2)
        self.set_comparator(-1, ch=1)
        self.set_comparator(-1, ch=2)
        self.set_mode(ch=1)
        self.set_mode(ch=2)
        self.enable_count(ch=1)
        self.enable_count(ch=2)
        self.set_z_mode(ch=1)
        self.set_z_mode(ch=2)
        return
    
    
    def _get_offset_for(self, ch, offset):
        ch_offset = {1: 0x00, 2: 0x10}
                
        if ch not in ch_offset:
            raise InvalidChannelError('ch must be 1 or 2, not {0}'.format(ch))
        
        return offset + ch_offset[ch]

        
    def reset(self, ch=1):
        """Reset count value for specified ch.
        Compatibility: PencReset function in GPG-6204 driver
        
        Parameters
        ----------
        ch : int (1:default or 2)
            Target channel number.
        """
        bar = 0
        offset = self._get_offset_for(ch, 0x06)
        
        flags = 'CC0 CC1'
        
        self.set_flag(bar, offset, flags)
        return

    
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
        bar = 0
        offset = self._get_offset_for(ch, 0x04)
        
        flags = mode
        if direction == 1: flags += ' DIR'
        if equal == 1: flags += ' EQS'
        
        self.set_flag(bar, offset, flags)
        return
    
    
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
        bar = 0
        offset = self._get_offset_for(ch, 0x04)
        size = 1
        
        return self.read(bar, offset, size)
    
    
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
        bar = 0
        offset = self._get_offset_for(ch, 0x07)
        
        flags = ' '.join([clear_condition, latch_condition])
        if z_polarity == 1: flags += ' ZP'
        
        self.set_flag(bar, offset, flags)
        return
        
    
    def get_z_mode(self, ch=1):
        """
        Compatibility: PencGetZMode function in GPG-6204 driver
        """
        bar = 0
        offset = self._get_offset_for(ch, 0x07)
        size = 1
        
        return self.read(bar, offset, size)
        
    
    def enable_count(self, ch=1):
        """
        Compatibility: PencEnableCount function in GPG-6204 driver
        """
        bar = 0
        offset = self._get_offset_for(ch, 0x05)
        
        flags = ''
        
        self.set_flag(bar, offset, flags)
        return
        
        
    def disable_count(self, ch=1):
        """
        Compatibility: PencEnableCount function in GPG-6204 driver
        """
        bar = 0
        offset = self._get_offset_for(ch, 0x05)
        
        flags = '/EN'
        
        self.set_flag(bar, offset, flags)
        return
   
        
    def set_counter_mode(self, ch=1):
        bar = 0
        offset = self._get_offset_for(ch, 0x05)
        
        flags = self.get_log('out', bar, offset).to_flags()
        flags = flags.replace('P/L', '')
        self.set_flag(bar, offset, flags)
        return
    

    def set_comparator_mode(self, ch=1):
        bar = 0
        offset = self._get_offset_for(ch, 0x05)
        
        flags = self.get_log('out', bar, offset).to_flags()
        flags += ' P/L'
        self.set_flag(bar, offset, flags)
        return
    

    def set_counter(self, count, ch=1):
        """
        Compatibility: PencSetCounter function in GPG-6204 driver
        """
        bar = 0
        offset = self._get_offset_for(ch, 0x00)
        size = 4
        
        d = struct.pack('<i', count)
        
        self.set_counter_mode()
        self.write(bar, offset, d)
        return
    
    
    def set_comparator(self, count, ch=1):
        """
        Compatibility: PencSetComparator function in GPG-6204 driver
        """
        bar = 0
        offset = self._get_offset_for(ch, 0x00)
        size = 4
        
        d = struct.pack('<i', count)
        
        self.set_comparator_mode()
        self.write(bar, offset, d)
        return
        
    
    def latch(self, ch=1):
        bar = 0
        offset = self._get_offset_for(ch, 0x06)
        
        flags = 'CC1'
        self.set_flag(bar, offset, flags)
        return
    
    
    def get_counter(self, ch=1):
        """
        Compatibility: PencGetCounter function in GPG-6204 driver
        """
        bar = 0
        offset = self._get_offset_for(ch, 0x00)
        size = 4
        
        self.set_counter_mode()
        self.latch(ch)
        d = self.read(bar, offset, size)
        d.set_fmt('<i')
        return d

    
    def get_status(self, ch=1):
        """
        Compatibility: PencGetStatus function in GPG-6204 driver
        """
        bar = 0
        offset = self._get_offset_for(ch, 0x05)
        size = 2
        
        d = self.read(bar, offset, size)
        return d
    


    
