
import time
import threading
import multiprocessing
import psutil
from . import core


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
        raise Exception('wrong range_ : %s'%(range_))
    
    ad_volt = adbit.to_int() * lsb + start
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

    available_ranges = [
        '0_5V',
        '0_10V',
        '2P5V',
        '5V',
        '10V',
    ]
    available_ad_channel_num = {'SINGLE': 64, 'DIFF': 32}
    available_di_channel_num = 2
    available_do_channel_num = 2
    
    _last_ch_no = -1
    _last_single_diff = ''
    conf = {}
    buffer = multiprocessing.Array('f', [])
    dtlog = multiprocessing.Array('f', [])
    smpl_status = 'STOP_SAMPLING'
    smpl_count = multiprocessing.Value('l', 0)
    flag_stop_sampling = multiprocessing.Value('b', True)
    
    def get_board_id(self):
        bar = 0
        offset = 0x17
        size = 1

        ret = self.read(bar, offset, size)
        bid = ret.to_hex()[1]

        return bid
    
    def initialize(self):
        self.stop_sampling()
        self.output_do([0, 0])
        self.clear_sampling_data()
        self._set_default_sampling_config()
        return
    
    def _set_default_sampling_config(self):
        self.conf = {
            'smpl_ch_req': [{'ch_no': i+1, 'range': '5V'} for i in range(64)],
            'sampling_mode': 'IO',
            'single_diff': 'SINGLE',
            'smpl_num': 1024,
            'smpl_event_num': 0, 
            'smpl_freq': 1.0,
            'trig_point': 'START',
            'trig_mode': 'FREERUN',
            'trig_delay': 0,
            'trig_ch': 1,
            'trig_level1': 0.0,
            'trig_level2': 0.0,
            'eclk_edge': 'DOWN',
            'atrg_pulse': 'LOW',
            'trig_edge': 'DOWN',
            'trig_di': 1,
            'fast_mode': 'NORMAL',
        }
        return
    
    def set_sampling_config(self, smpl_ch_req=None, sampling_mode=None, single_diff=None,
                            smpl_num=None, smpl_event_num=None, smpl_freq=None,
                            trig_point=None, trig_mode=None, trig_delay=None,
                            trig_ch=None, trig_level1=None, trig_level2=None,
                            eclk_edge=None, atrg_pulse=None, trig_edge=None,
                            trig_di=None, fast_mode=None):
        self.conf = {
            'smpl_ch_req': smpl_ch_req if smpl_ch_req is not None else self.conf['smpl_ch_req'],
            'sampling_mode': sampling_mode if sampling_mode is not None else self.conf['sampling_mode'],
            'single_diff': single_diff if single_diff is not None else self.conf['single_diff'],
            'smpl_num': smpl_num if smpl_num is not None else self.conf['smpl_num'],
            'smpl_event_num': smpl_event_num if smpl_event_num is not None else self.conf['smpl_event_num'],
            'smpl_freq': smpl_freq if smpl_freq is not None else self.conf['smpl_freq'],
            'trig_point': trig_point if trig_point is not None else self.conf['trig_point'],
            'trig_mode': trig_mode if trig_mode is not None else self.conf['trig_mode'],
            'trig_delay': trig_delay if trig_delay is not None else self.conf['trig_delay'],
            'trig_ch': trig_ch if trig_ch is not None else self.conf['trig_ch'],
            'trig_level1': trig_level1 if trig_level1 is not None else self.conf['trig_level1'],
            'trig_level2': trig_level2 if trig_level2 is not None else self.conf['trig_level2'],
            'eclk_edge': eclk_edge if eclk_edge is not None else self.conf['eclk_edge'],
            'atrg_pulse': atrg_pulse if atrg_pulse is not None else self.conf['atrg_pulse'],
            'trig_edge': trig_edge if trig_edge is not None else self.conf['trig_edge'],
            'trig_di': trig_di if trig_di is not None else self.conf['trig_di'],
            'fast_mode': fast_mode if fast_mode is not None else self.conf['fast_mode'],
        }
        return
            
    def get_sampling_config(self):
        return self.conf
        
    def get_sampling_data(self, smpl_num):
        raise NotImplemented()
        self.smpl_count -= smpl_num
        return [self.buffer.pop(0) for i in range(smpl_num)]
    
    def read_sampling_buffer(self, smpl_num, offset):
        buffer_1 = list(self.buffer)
        blen = len(buffer_1)
        ddlen = len(self.conf['smpl_ch_req'])
        buffer_ = [buffer_1[i*ddlen:(i+1)*ddlen] for i in range(blen//ddlen)]
        dlen = len(buffer_)

        if offset < 0:
            offset = dlen + offset
            pass
        
        if smpl_num + offset < dlen:
            return buffer_[offset:offset+smpl_num]
        
        d1 = buffer_[offset:]
        d2 = buffer_[:smpl_num+offset-dlen]
        return d1 + d2
    
    def clear_sampling_data(self):
        self.stop_sampling()
        self.buffer = multiprocessing.Array('f', [])
        self.dtlog = multiprocessing.Array('f', [])
        self.smpl_count.value = 0
        self.flag_stop_sampling.value = True
        self.smpl_status = 'STOP_SAMPLING'
        return
    
    def start_sampling(self, sync_flag):
        if self.flag_stop_sampling.value == False:
            return
        
        self.buffer = multiprocessing.Array('f', self.conf['smpl_num'] * len(self.conf['smpl_ch_req']))
        self.dtlog = multiprocessing.Array('f', [0 for _ in range(self.conf['smpl_num'])])
        self.flag_stop_sampling.value = False
        self.smpl_count.value = 0

        sampling_proc = multiprocessing.Process(target=sampling_loop,
                                                args=[self, self.buffer, self.dtlog,
                                                      self.flag_stop_sampling,
                                                      self.smpl_count])
        
        sampling_proc.start()
        sampling_putil = psutil.Process(sampling_proc.pid)
        sampling_putil.nice(-20)
        
        self.smpl_status = 'NOW_SAMPLING'
        
        if sync_flag == 'SYNC':
            sampling_proc.join()
            pass
        
        return

    def trigger_sampling(self, ch_no, smpl_num):
        raise NotImplementedError()
    
    def stop_sampling(self):
        self.flag_stop_sampling.value = True
        self.smpl_status = 'STOP_SAMPLING'
        return
    
    def get_status(self):
        if self.flag_stop_sampling.value == True:
            self.smpl_status = 'STOP_SAMPLING'
            pass
        
        d = {
            'smpl_status': self.smpl_status,
            'smpl_count': self.smpl_count.value,
            'avail_count': len(self.buffer)//len(self.conf['smpl_ch_req']) - self.smpl_count.value,
        }
        return d
    
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
        while self._is_busy():
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
            raise Exception('wrong single_diff: %s'%single_diff)
        
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
    
    def _set_ch_and_start_adc(self, ch):
        bar = 0
        size = 1
        offset = 0x04
        
        ch_bitlist = ch2bitlist(ch)
        
        if ch == self._last_ch_no:
            mode = [1, 0]
        else:
            mode = [0, 0]
            pass
        
        d = ch_bitlist + mode
        
        self._wait_operation_stop()
        self.write(bar, offset, core.list2bytes(d))
        self._last_ch_no = ch
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
        


def sampling_loop(ad, buffer_, dtlog, flag_stop_sampling, smpl_count):
    dt = 1 / ad.conf['smpl_freq']
    t0 = time.time()
    dlen = len(ad.conf['smpl_ch_req'])
    
    while True:
        d = ad.input_ad(ad.conf['single_diff'], ad.conf['smpl_ch_req'])
        
        for i in range(dlen):
            buffer_[smpl_count.value * dlen + i] = d[i]
            continue
        
        with smpl_count.get_lock():
            smpl_count.value += 1
            pass
        
        if smpl_count.value >= ad.conf['smpl_num']:
            if ad.conf['trig_mode'] != 'ETERNITY':
                break
            else:
                smpl_count.value = 0
                pass
            pass
        
        rest = dt - (time.time() - t0)
        if rest > 1e-4:
            time.sleep(rest - 1e-4)
            pass
        
        t1 = time.time()
        dtlog[smpl_count.value-1] = t1 - t0
        t0 = t1
        
        if flag_stop_sampling.value:
            break
        
        continue
    
    flag_stop_sampling.value = True
    return
    
