
"""
PCI/CPZ-2724 DIO ボードのドライバです。概ね公式ドライバ GPG-2000 に対応する機能を提供します。


メソッド一覧
----------

.. list-table:: 
  :header-rows: 1

  * - メソッド
    - 公式ドライバの対応する関数
    - 機能
  
  * - `initialize() <#pyinterface.pci2724.pci2724_driver.initialize>`_
    - DioOpen
    - ボードを初期化します

  * - `input_point(start, num) <#pyinterface.pci2724.pci2724_driver.input_point>`_
    - DioInputPoint
    - デジタル入力を任意点数取得します

  * - `input_byte(range_) <#pyinterface.pci2724.pci2724_driver.input_byte>`_
    - DioInputByte
    - デジタル入力を1byte単位で取得します

  * - `input_word(range_) <#pyinterface.pci2724.pci2724_driver.input_word>`_
    - DioInputWord
    - デジタル入力を2byte単位で取得します

  * - `input_dword() <#pyinterface.pci2724.pci2724_driver.input_dword>`_
    - DioInputDword
    - デジタル入力を4byte単位で取得します

  * - `output_point(data, start) <#pyinterface.pci2724.pci2724_driver.output_point>`_
    - DioOutputPoint
    - デジタル出力を任意点数設定します

  * - `output_byte(range_) <#pyinterface.pci2724.pci2724_driver.output_byte>`_
    - DioOutputByte
    - デジタル出力を1byte単位で設定します

  * - `output_word(range_) <#pyinterface.pci2724.pci2724_driver.output_word>`_
    - DioOutputWord
    - デジタル出力を2byte単位で設定します

  * - `output_dword() <#pyinterface.pci2724.pci2724_driver.output_dword>`_
    - DioOutputDword
    - デジタル出力を4byte単位で設定します
 
  * - `set_latch_status(enable) <#pyinterface.pci2724.pci2724_driver.set_latch_status>`_
    - DioSetLatchStatus
    - ラッチ回路の接続を設定します

  * - `get_latch_status() <#pyinterface.pci2724.pci2724_driver.get_latch_status>`_
    - DioGetLatchStatus
    - ラッチ回路の接続状態を取得します

  * - `get_ack_status() <#pyinterface.pci2724.pci2724_driver.get_ack_status>`_
    - DioGetAckStatus
    - ACK2, STB2 端子の接続状態を取得します

  * - `set_ack_pulse_command(ack, pulse) <#pyinterface.pci2724.pci2724_driver.set_ack_pulse_command>`_
    - DioSetAckPulseCommand
    - ACK1, PULS.OUT1 の出力制御を設定します

  * - `get_stb_status() <#pyinterface.pci2724.pci2724_driver.get_stb_status>`_
    - DioGetStbStatus
    - STB1, ACK1 端子の接続状態を取得します

  * - `set_stb_pulse_command(stb, pulse) <#pyinterface.pci2724.pci2724_driver.set_stb_pulse_command>`_
    - DioSetStbPulseCommand
    - STB2, PULS.OUT2 の出力制御を設定します


I/O ポート
---------

.. list-table:: 
  :header-rows: 1

  * - ポート名
    - 説明

  * - `pci2724_in <#pyinterface.pci2724.pci2724_in>`_
    - PCI2724 I/O 入力ポート (16bytes)

  * - `pci2724_out <#pyinterface.pci2724.pci2724_out>`_
    - PCI2724 I/O 出力ポート (16bytes)
  

"""

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
        """ボードを初期化します
        
        Notes
        -----
        - 以下の処理を実行します:
        
            - デジタル出力の解除
            - ラッチ出力の解除
        
        - DioOpen 関数に概ね対応しますが、pyinterface には open の概念がありませんので
          initialize() を実行しなくともドライバへアクセス可能です。
        - initialize() を実行しない場合、直前のボード状況が反映されています。
        """
        self.bytes_in[0].set(0)
        self.bytes_out[0].set(0)
        self.output_dword([0]*32)
        self.set_latch_status()
        return

    def input_point(self, start, num):
        """デジタル入力を任意点数取得します
        
        Notes
        -----
        GPG-2000ドライバのDioInputPoint関数に対応します
        
        Parameters
        ----------
        start : int
            取得する最初のチャンネルを指定します (範囲: 1 -- 32)
        num : int
            取得する個数を指定します (`start` + `num` が 33 を超えてはいけません) 
        
        Returns
        -------
        list
            指定したチャンネルのデジタル入力状況のリスト
        
        Examples
        --------
        IN2 - IN6 のデジタル入力状況を取得します
        
        >>> pci2724.input_point(2, 5)
        [1, 0, 1, 0, 1]
        """
        self._verify_io_number_access(start, num)
        inp = self._get_input()
        bits_str = inp.ordered_bit()
        bits = list(map(int, bits_str[start-1:start+num-1]))
        return bits

    def output_point(self, data, start):
        """デジタル出力を任意点数設定します
        
        Notes
        -----
        GPG-2000ドライバのDioOutputPoint関数に対応します
        
        Parameters
        ----------
        data : list
            設定するデジタル出力状況のリストです (1:ON, 0:OFF)
        start : int
            設定する最初のチャンネルを指定します (範囲: 1 -- 32)
        
        Returns
        -------
        pyinterface.core.Bytes
            デジタル出力状況
        
        Examples
        --------
        OUT3 より 4 チャンネルのデジタル出力を ON にします
        
        >>> pci2724.output_point([1,1,1,1], 3)
        3C000000
        """
        return self._set_output(data, start_num)

    def input_byte(self, range_):
        """デジタル入力を1byte単位で取得します
        
        Notes
        -----
        GPG-2000ドライバのDioInputByte関数に対応します
        
        Parameters
        ----------
        range_ : str
            デジタル入力状況を取得する範囲を指定します
            
            .. list-table:: 
                :header-rows: 1
        
                * - `range_`
                  - 取得するチャンネル
  
                * - 'IN1_8' 
                  - IN1 から IN8 まで
        
                * - 'IN9_16' 
                  - IN9 から IN16 まで
        
                * - 'IN17_24' 
                  - IN17 から IN24 まで
        
                * - 'IN25_32' 
                  - IN25 から IN32 まで
        
        Returns
        -------
        list
            指定したチャンネルのデジタル入力状況のリスト (length=8)
        
        Examples
        --------
        IN9 - IN16 のデジタル入力状況を取得します
        
        >>> pci2724.input_byte('IN9_16')
        [1, 1, 0, 0, 1, 0, 1, 0]
        """
        if isinstance(range_, str):
            if range_.find('IN1_8') != -1: start = 1
            elif range_.find('IN9_16') != -1: start = 9
            elif range_.find('IN17_24') != -1: start = 17
            elif range_.find('IN25_32') != -1: start = 25
            else: return
        
        if isinstance(range_, int):
            start = range_
            pass
        
        num = 8
            
        self._verify_io_number_access(start, num)
        inp = self._get_input()
        bits_str = inp.ordered_bit()
        bits = list(map(int, bits_str[start-1:start+num-1]))
        return bits
    
    def input_word(self, range_):
        """デジタル入力を2byte単位で取得します
        
        Notes
        -----
        GPG-2000ドライバのDioInputWord関数に対応します
        
        Parameters
        ----------
        range_ : str
            デジタル入力状況を取得する範囲を指定します
            
            .. list-table:: 
                :header-rows: 1
        
                * - `range`
                  - 取得するチャンネル
  
                * - 'IN1_16' 
                  - IN1 から IN16 まで
        
                * - 'IN17_32' 
                  - IN17 から IN32 まで
        
        Returns
        -------
        list
            指定したチャンネルのデジタル入力状況のリスト (length=16)
        
        Examples
        --------
        IN1 - IN16 のデジタル入力状況を取得します
        
        >>> pci2724.input_word('IN1_16')
        [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0]
        """
        if isinstance(range_, str):
            if range_.find('IN1_16') != -1: start = 1
            elif range_.find('IN17_32') != -1: start = 17
            else: return
        
        if isinstance(range_, int):
            start = range_
            pass
            
        num = 16
            
        self._verify_io_number_access(start, num)
        inp = self._get_input()
        bits_str = inp.ordered_bit()
        bits = list(map(int, bits_str[start-1:start+num-1]))
        return bits

    def input_dword(self):
        """デジタル入力を4byte取得します
        
        Notes
        -----
        GPG-2000ドライバのDioInputDword関数に対応します
        
        Returns
        -------
        list
            デジタル入力状況のリスト (length=32)
        
        Examples
        --------
        IN1 - IN32 のデジタル入力状況を取得します
        
        >>> pci2724.input_dword()
        [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0,
         1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0]
        """
        self._verify_io_number_access(1, 32)
        inp = self._get_input()
        bits_str = inp.ordered_bit()
        bits = list(map(int, bits_str[0:32]))
        return bits

    def output_byte(self, data, range_):
        """デジタル出力を1byte単位で設定します
        
        Notes
        -----
        GPG-2000ドライバのDioOutputByte関数に対応します
        
        Parameters
        ----------
        data : list
            設定するデジタル出力状況のリストです (1:ON, 0:OFF)。length は 8 にしてください。
        range_ : str
            デジタル出力状況を設定する範囲を指定します
            
            .. list-table:: 
                :header-rows: 1
        
                * - `range_`
                  - 設定するチャンネル
  
                * - 'OUT1_8' 
                  - OUT1 から OUT8 まで
        
                * - 'OUT9_16' 
                  - OUT9 から OUT16 まで
        
                * - 'OUT17_24' 
                  - OUT17 から OUT24 まで
        
                * - 'OUT25_32' 
                  - OUT25 から OUT32 まで
        
        Returns
        -------
        pyinterface.core.Bytes
            デジタル出力状況
        
        Examples
        --------
        OUT1 より 1 byte 分のチャンネルのデジタル出力を設定します
        
        >>> pci2724.output_byte([1,0,1,0,1,0,1,0], 'OUT1_8')
        55000000
        """
        if len(data) != 8:
            msg = 'data length should be 8'
            msg += ' while {0} length list is given.'.format(len(data))
            raise InvalidListLengthError(msg)
        
        if isinstance(range_, str):
            if range_.find('OUT1_8') != -1: range_ = 1
            elif range_.find('OUT9_16') != -1: range_ = 9
            elif range_.find('OUT17_24') != -1: range_ = 17
            elif range_.find('OUT25_32') != -1: range_ = 25
            else: return
            
        return self._set_output(data, range_)

    def output_word(self, data, range_):
        """デジタル出力を2byte単位で設定します
        
        Notes
        -----
        GPG-2000ドライバのDioOutputWord関数に対応します
        
        Parameters
        ----------
        data : list
            設定するデジタル出力状況のリストです (1:ON, 0:OFF)。length は 16 にしてください。
        range_ : str
            デジタル出力状況を設定する範囲を指定します
            
            .. list-table:: 
                :header-rows: 1
        
                * - `range_`
                  - 設定するチャンネル
  
                * - 'OUT1_16'
                  - OUT1 から OUT16 まで
        
                * - 'OUT17_32'
                  - OUT17 から OUT32 まで
        
        Returns
        -------
        pyinterface.core.Bytes
            デジタル出力状況
        
        Examples
        --------
        OUT17 より 2 byte 分のチャンネルのデジタル出力を設定します
        
        >>> pci2724.output_word([1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0], 'OUT17_32')
        0000550F
        """
        if len(data) != 16:
            msg = 'data length should be 16'
            msg += ' while {0} length list is given.'.format(len(data))
            raise InvalidListLengthError(msg)
        
        if isinstance(range_, str):
            if range_.find('OUT1_16') != -1: range_ = 1
            elif range_.find('OUT17_32') != -1: range_ = 17
            else: return
            
        return self._set_output(data, range_)

    def output_dword(self, data):
        """デジタル出力を4byte設定します
        
        Notes
        -----
        GPG-2000ドライバのDioOutputDword関数に対応します
        
        Parameters
        ----------
        data : list
            設定するデジタル出力状況のリストです (1:ON, 0:OFF)。length は 32 にしてください。
        
        Returns
        -------
        pyinterface.core.Bytes
            デジタル出力状況
        
        Examples
        --------
        OUT1 より 4byte 分のチャンネルのデジタル出力を設定します
        
        >>> d = [1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0]
        >>> pci2724.output_dword(d)
        550F550F
        """
        if len(data) != 32:
            msg = 'data length should be 32'
            msg += ' while {0} length list is given.'.format(len(data))
            raise InvalidListLengthError(msg)
        
        return self._set_output(data, 1)
    
    def set_latch_status(self, enable=''):
        """ラッチ回路の接続を設定します
        
        Notes
        -----
        Compatibility: DioSetLatchStatus function in GPG-2000 driver
        
        Parameters
        ----------
        enable : str
            ラッチ回路接続を有効にするポートを指定します。
            複数指定する場合、スペースで区切って指定してください。
            指定されなかったポートは、ラッチ回路接続 "無効" になります。
        
            .. list-table:: 
                :header-rows: 1
                
                * - `enable`
                  - 有効にするチャンネル
                
                * - 'PORT0'
                  - IN1 - IN8
            
                * - 'PORT1'
                  - IN9 - IN16
            
                * - 'PORT2'
                  - IN17 - IN24 
        
                * - 'PORT3'
                  - IN25 - IN32
        
        Examples
        --------
        pci2724.set_latch_status('PORT0 PORT3')
        """
        addr = 0x0b
        flags = enable
        return self._set_register(addr, flags)
    
    def get_latch_status(self):
        """ラッチ回路の接続を取得します
        
        Notes
        -----
        Compatibility: DioGetLatchStatus function in GPG-2000 driver
        """
        addr = 0x0b
        return self._get_register(addr)
    
    def get_ack_status(self):
        """ACK2, STB2 端子の接続状態を取得します

        Notes
        -----
        Compatibility: DioGetAckStatus function in GPG-2000 driver
        """
        addr = 0x08
        return self._get_register(addr)
    
    def set_ack_pulse_command(self, ack='', pulse=''):
        """ACK1, PULS.OUT1 の出力制御を設定します

        Notes
        -----
        Compatibility : DioSetAckPulseCommand function in GPG-2000 driver
        
        Parameters
        ----------
        ack : str 
            ACK 出力制御
        
            .. list-table:: 
                :header-rows: 1
         
                * - `ack`
                  - 動作
        
                * - ''
                  - 何もしません
        
                * - 'ACK10'
                  - clear ACK1 terminal (Low -> High)
        
                * - 'ACK11'
                  - set ACK1 terminal (High -> Low)
        
        pulse : str
            PULSE.OUT1 出力制御
        
            .. list-table:: 
                :header-rows: 1
         
                * - `pulse`
                  - 動作
        
                * - ''
                  - 何もしません
        
                * - 'PO10'
                  - set PULS.OUT1 terminal High
        
                * - 'PO11'
                  - set PULS.OUT1 terminal Low
        
                * - 'PO12'
                  - output Low pulse from PULS.OUT1 terminal
        """
        addr = 0x08
        flags = ack + ' ' + pulse
        return self._set_register(addr, flags)
    
    def get_stb_status(self):
        """STB1, ACK1 端子の接続状態を取得します
        
        Notes
        -----
        Compatibility: DioGetStbStatus function in GPG-2000 driver
        """
        addr = 0x09
        return self._get_register(addr)
        
    def set_stb_pulse_command(self, stb='', pulse=''):
        """STB2, PULS.OUT2 の出力制御を設定します
        
        Notes
        -----
        Compatibility : DioSetStbPulseCommand function in GPG-2000 driver
        
        Parameters
        ----------
        stb : str
            STB 出力制御
        
            .. list-table:: 
                :header-rows: 1
         
                * - `stb`
                  - 動作
        
                * - ''
                  - 何もしません
        
                * - 'STB20'
                  - clear STB2 terminal (Low -> High)

                * - 'STB21'
                  - set STB2 terminal (High -> Low)
        
        pulse : str
            PULSE.OUT2 出力制御
        
            .. list-table:: 
                :header-rows: 1
         
                * - `pulse`
                  - 動作
        
                * - ''
                  - 何もしません
        
                * - 'PO20'
                  - set PULS.OUT2 terminal High
        
                * - 'PO21'
                  - set PULS.OUT2 terminal Low

                * - 'PO22'
                  - output Low pulse from PULS.OUT2 terminal
        """
        addr = 0x09
        flags = stb + ' ' + pulse
        return self._set_register(addr, flags)

    
