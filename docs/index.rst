.. pyinterface documentation master file, created by
   sphinx-quickstart on Wed Nov 29 03:13:28 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyinterface : Interface PCI ボードドライバ
========================================

これは何か
--------

- `pyinterface <https://github.com/ars096/pyinterface2>`_ は、`株式会社 Interface <http://www.interface.co.jp/>`_ が提供するPCIボードのLinux/Python向けドライバです (pyinterfaceはInterface社とは関係ありません)
- PCIのI/Oポートに直接アクセスするため、公式のドライバを使わずに動作します

  - 公式ドライバではサポート外の最新のLinuxディストリビューションでも利用可能です
  - I/Oポートアクセスに `PortIO <http://portio.inrim.it/>`_ モジュールを使用しています


動作環境
^^^^^^^
- Linux (x86 architecture)
- Python 3.0+


必要なモジュール
^^^^^^^^^^^^^
- `PortIO <http://portio.inrim.it/>`_


使い方
-----

インストール方法
^^^^^^^^^^^^^

::

    pip install pyinterface


初めの一歩
^^^^^^^^

pyinterface では、PCIのI/Oポートに直接アクセスするために、`iopl <https://linuxjm.osdn.jp/html/LDP_man-pages/man2/iopl.2.html>`_ を使用するため、root権限を必要とします。以下の例は、sudo ipython などとしてroot権限で実行してください。

.. code-block:: python

    import pyinterface
    
    board_name = 2724  # 使用するボードの型番 : 例. PCI/CPZ-2724 (DIOボード)
    rsw_id = 2         # 本体ボードに設定しているRSW1の番号 : 例. 2 を設定している
    
    # ボードを open
    b = pyinterface.open(board_name, rsw_id)
    
    # digital input 状況を取得
    b.input_byte('IN1_8')
    >>> [0, 0, 0, 0, 0, 0, 0, 0]
    
    # digital output を設定
    b.output_byte([0, 1, 0, 1, 0, 0, 1, 1], 'OUT25_32')
    >>> 000000CA


ボード別の使用方法
^^^^^^^^^^^^^^^

以下のボードについて、ドライバを提供しています。

- `PCI/CPZ-2724 <pyinterface.pci2724.html>`_
- `PCI/CPZ-6204 <pyinterface.pci6204.html>`_



API ドキュメント
--------------

.. toctree::
   :maxdepth: 4

   pyinterface


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

