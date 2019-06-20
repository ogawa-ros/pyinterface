
import time
import struct
from . import core


ad_mode = {'single':64, 'diff':32}
inputrange_list = ['AD0_5V', 'AD0_10V', 'AD-2.5_2.5V', 'AD-5_5V', 'AD-10_10V']


class InvalidChError(Exception):
    pass

class InvalidModeError(Exception):
    pass

class InvalidInputrangeError(Exception):
    pass



def ch2bitlist(ch):
    ch_bit = '{0:06b}'.format(ch-1)
    ch_bitlist = [int(_b) for _b in ch_bit[::-1]]
    return ch_bitlist
    
def decode_adbit(adbit, range_):
    if range_ == '0_5V':
        lsb = 5 / 4096
        start = 0
    elif range_ == '0_10V':
        lsb = 10 / 4096
        start = 0
    elif range_ == '2P5V':
        lsb = 5 / 4096
        start = -2.5
    elif range_ == '5V':
        lsb = 10 / 4096
        start = -5
    elif range_ == '10V':
        lsb = 20 / 4096
        start = -10
    else:
        raise('wrong range_ : %s'%(range_))
    
    ad_volt = adbit.to_int() * lsb - start
    return ad_volt
    


class pci3177_driver(core.interface_driver):
    bit_flags_in = (
        (
            ('B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'),
            ('B8', 'B9', 'B10', 'B11', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', 'BUSY'),
            ('CA0', 'CA1', 'CA2', 'CA3', 'CA4', 'CA5', '', ''),
            ('SD0', 'SD1', 'SD2', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('GATE', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('TMR', 'BSY', 'TRG', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('TMR', 'BSY', 'TRG', '', '', '', '', ''),
            ('EXTG', 'EINT', '', '', '', '', '', 'DITG'),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('BID0', 'BID1', 'BID2', 'BID3', 'M/S', 'CLKOEN', 'TRGOEN', ''),
            ('', '', '', '', '', '', 'SMD0', 'SMD1'),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('IN1', 'IN2', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '')
        ),
        (
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', '')
        )
    )

    bit_flags_out = (
        (
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('CA0', 'CA1', 'CA2', 'CA3', 'CA4', 'CA5', 'MA', 'MB'),
            ('SD0', 'SD1', 'SD2', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('GATE', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('DITG', 'TMR', 'BSY', 'TRG', '', '', '', ''),
            ('', 'EXTG', 'EINT', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('SMD1', '', '', '', '', 'M/S', 'CLKOEN', 'TRGOEN'),
            ('', '', '', '', '', '', '', 'SMD0'),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '', ''),
            ('OUT1', 'OUT2', '', '', '', '', '', ''),
            ('', '', '', '', '', '', '')
        ),
        (
            ('', '', '', '', '', '', '', ''),
            ('U/D', 'INC', 'CS', '', '', '', '', ''),
            ('U/D', 'INC', 'CS', '', '', '', '', ''),
            ('U/D', 'INC', 'CS', '', '', '', '', '')
        )
    )
    
    _last_ch_no = -1
    _last_single_diff = ''
    
    def get_board_id(self):
        bar = 0
        offset = 0x17
        size = 1

        ret = self.read(bar, offset, size)
        bid = ret.to_hex()[1]

        return bid
    
    def initialize(self):
        pass
    
    
    def set_sampling_config(self, smpl_ch_req, sampling_mode, 
                            single_diff, smpl_num, smpl_event_num, smpl_freq,
                            trig_point, trig_mode, trig_delay, trig_ch,
                            trig_level1, trig_level2, eclk_edge, atrg_pulse,
                            trig_edge, trig_di, fast_mode):
        pass
    
    def get_sampling_config(self):
        pass
        
    def get_sampling_data(self, smpl_num):
        pass
    
    def read_sampling_buffer(self, smpl_num, offset):
        pass
    
    def clear_sampling_data(self):
        pass
    
    def start_sampling(self, sync_flag):
        pass
    
    def trigger_sampling(self, ch_no, smpl_num):
        pass
    
    def stop_sampling(self):
        pass
    
    def get_status(self):
        pass
    
    def input_ad(self, single_diff, smpl_ch_req):
        self._set_single_diff(single_diff)
        d = [self._get_ad_oneshot(r['ch_no'], r['range'])
             for r in smpl_ch_req]
        return d
    
    def input_di(self):
        bar = 0
        size = 1
        offset = 0x1e
        
        di = self.read(bar, offset, size)
        di_list = di.to_list()[:2]
        return di_list
        
    def output_do(self, do_list):
        bar = 0
        size = 1
        offset = 0x1e
        
        do_list2 = do_list + [0]*(8-len(do_list))
        self.write(bar, offset, core.list2bytes(do_list2))
        return
        
    

    def _wait_operation_stop(self):
        while not self._is_busy():
            time.sleep(1e-6)
            continue
        return

    def _get_ad_oneshot(self, ch, range_):
        self._set_ch_and_start_adc(ch)
        ad_bit = self._get_data()
        ad_volt = decode_adbit(ad_bit, range_)
        return ad_volt

    def _set_single_diff(self, single_diff):
        if single_diff == self._last_single_diff:
            return
        
        if single_diff == 'SINGLE':
            flag = ''
        elif single_diff == 'DIFF':
            flag = 'SD0'
        else:
            raise('wrong single_diff: %s'%single_diff)
        
        self._set_input_config(flag)
        self._last_single_diff = single_diff
        return


    def _is_busy(self):
        bar = 0
        size = 1
        offset = 0x03
        
        is_idle = self.read(bar, offset, size)[7]
        is_busy = not is_idle
        return is_busy
    
    def _set_ch_and_start_adc(self, ch_req):
        bar = 0
        size = 1
        offset = 0x04
        
        ch_bitlist = ch2bitlist(ch['ch_no'])
        
        if ch['ch_no'] == self._last_ch_no:
            mode = [1, 0]
        else:
            mode = [0, 0]
            pass
        
        d = ch_bitlist + mode
        
        self._wait_operation_stop()
        self.write(bar, offset, core.list2bytes(d))
        self._last_ch_no = ch['ch_no']
        return
    
    def _get_data(self):
        bar = 0
        size = 2
        offset = 0x00
        
        self._wait_operation_stop()
        data = self.read(bar, offset, size)
        return data
    
    def _read_input_config(self):
        bar = 0
        size = 1
        offset = 0x05
        
        d = self.read(bar, offset, size)
        return d
        
    def _set_input_config(self, flag):
        bar = 0
        size = 1
        offset = 0x05
        
        self.set_flag(bar, offset, flag)
        return
        


