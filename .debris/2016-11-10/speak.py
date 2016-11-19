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

import os 


def speak_text(tospeak, countrycode='de'):
    """
    Function to speak out some text
    :param tospeak: the text you want to speak out
    :param countrycode: countrycode of language you want to use
    """
    os.system("espeak -v{} {}".format(countrycode, str(tospeak)))

