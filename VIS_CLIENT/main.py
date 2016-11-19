#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""VIS-CLIENT.py:	Description of VIS-CLIENT.py"""

__author__ = "Marc Steinebrunner"
__copyright__ = ""
__credits__ = "Raphael Kreft, HackersHous"

__license__ = ""
__version__ = "0.0.3"
__email__ = "marc.steinebrunner@gmail.com"
__status__ = "In Process"

import PY.config
import sys
import socket
from PY.log import Log
from UI.PY.vision import Vision
from UI.PY.speech import Speech
from UI.PY.nlg_lite import acknowledge
from PY.comm import Comm

class Main(self):

    _my_name = my_name
    _launch_phrase = launch_phrase
    _portVISClient = portVISClient
    _hostVISServer = hostVISServer
    _portInput = portInput
    _hostInput = hostInput
    _portOutput = portOutput
    _hostOutput = hostOutput
    _use_launch_phrase = use_launch_phrase
    _debugger_enabled = debugger_enabled
    _camera = camera


    def __init__(self):
        self.speech = Speech(launch_phrase=launch_phrase, debugger_enabled=debugger_enabled)
        self.vision = Vision(camera=camera)

    def start(self):
        while True:
            if self.vision.recognize_face():
                recognizer,audio = self.speech.listen_for_audio()
                if self.speech.is_call_to_action(recognizer, audio):
                    self.__acknowledge_action()
                    self.decide_action()
                else:
                    self.decide_action()

    def decide_action(self):
        recognizer, audio = self.speech.listen_for_audio()

        speech = self.speech.google_speech_recognition(recognizer, audio)
        host = hostVISServer
        port = portVISClient
        message = speech
        Comm.client(host, port, message)

        message = Log
        Log.log_in(Log)

        self.speech.synthesize_text(data)

    def __acknowledge_action(self):
        self.__text_action(self.nlg_lite.acknowledge())

    def __text_action(self, text=None):
        if text is not None:
            text = PRINT
            Log.log_out(PRINT)
            PRINT = text
            self.speech.synthesize_text(text)

if __name__ == "__main__":
    main = Main()
    main.start()
