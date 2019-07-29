
"""
公式ドライバ GPG-7400 に対応するインターフェースです。
各機能の実装は、個別のボードのドライバにあります。


メソッド一覧
----------

"""

class gpg7400(object):

    motion = {
        'x': {
            'clock':  0,
            'acc_mode': '',
            'low_speed': 0,
            'speed': 0,
            'acc': 0,
            'dec': 0,
            'step': 0
        },
        'y': {
            'clock':  0,
            'acc_mode': '',
            'low_speed': 0,
            'speed': 0,
            'acc': 0,
            'dec': 0,
            'step': 0
        },
        'z': {
            'clock':  0,
            'acc_mode': '',
            'low_speed': 0,
            'speed': 0,
            'acc': 0,
            'dec': 0,
            'step': 0
        },
        'u': {
            'clock':  0,
            'acc_mode': '',
            'low_speed': 0,
            'speed': 0,
            'acc': 0,
            'dec': 0,
            'step': 0
        }
    }

    def __init__(self, driver):
        self.driver = driver
        pass


    def initialize(self):
        """ボードを初期化します
        
        - DioOpen 関数に概ね対応しますが、pyinterface には open の概念がありませんので
          initialize() を実行しなくともドライバへアクセス可能です。
        - initialize() を実行しない場合、直前のボード状況が反映されています。
        """
        self.driver.initialize()
        return


    def reset(self, axis, mode):
        """ボードの設定をリセットします。
        (GPG-7400 3. MtnReset)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        self.driver.reset(axis, mode)
        return


    def set_motion(self, axis, mode, motion):
        """各軸に独立動作パラメータを設定します。
        (GPG-7400 11. MtnSetMotion)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        self.driver.set_motion(axis, mode, motion)
        return


    def get_motion(self, axis, mode):
        """各軸の独立動作パラメータを取得します。
        (GPG-7400 23. MtnGetMotion)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        ret = self.driver.get_motion(axis, mode)
        return ret


    def start_motion(self, axis, start_mode, move_mode):
        """各種モータ動作を起動します。
        (GPG-7400 28. MtnStartMotion)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        self.driver.start_motion(axis, start_mode, move_mode)
        return


    def stop_motion(self, axis, stop_mode):
        """動作を停止させます。
        (GPG-7400 29. MtnStopMotion)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        self.driver.stop_motion(axis, stop_mode)
        return


    def change_speed(self, axis, mode, speed):
        """動作中に速度パターン変更を行います。
        (GPG-7400 33. MtnChangeSpeed)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        self.driver.change_speed(axis, mode, speed)
        return


    def change_step(self, axis, step):
        """動作中に目標位を変更します。(PTP 動作実行中のみ実行可能)
        (GPG-7400 34. MtnChangeStep)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        self.driver.change_step(axis, step)
        return


    def read_speed(self, axis):
        """現在の移動速度を取得します。
        (GPG-7400 36. MtnReadSpeed)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        ret = self.driver.read_speed(axis)
        return ret


    def read_counter(self, axis, cnt_mode):
        """各種カウンタ地の読み込みを行います。
        (GPG-7400 37. MtnReadCounter)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        ret = self.driver.read_counter(axis, cnt_mode)
        return ret


    def write_counter(self, axis, cnt_mode, counter):
        """各種カウンタ地の読み込みを行います。
        (GPG-7400 38. MtnWriteCounter)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        self.driver.write_counter(axis, cnt_mode, counter)
        return


    def output_do(self, do):
        """汎用出力 (DO1 ~ DO4)を制御します。
        (GPG-7400 39. MtnOutputDO)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        self.driver.output_do(do)
        return


    def input_di(self):
        """入力 (DI1 ~ DI12) の状態を取得します。
        (GPG-7400 40. MtnInputDI)

        Parameters
        ----------
        ...

        Returns
        -------
        ...

        Examples
        --------
        ...

        Exceptions
        ----------
        ...
        """
        data = self.driver.input_di()
        return data


