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
import config
import sys
import socket
from vision import Vision
from speech import Speech
from nlg_lite import acknowledge
from comm import Client

class Main(self):

config()

_my_name = my_name
_launch_phrase = launch_phrase
_portVISClient = portVISClient
_hostVISServer = hostVISServer
_portVisable = portVisable
_hostVisable = hostVisable
_use_launch_phrase = use_launch_phrase
_debugger_enabled = debugger_enabled
_camera = camera


    def __init__(self):
        self.speech = Speech(launch_phrase=launch_phrase, debugger_enabled=debugger_enabled)
        self.vision = Vision(camera=camera)

    def start(self):
        while True:
            requests.get("http://localhost:8080/clear")
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

        s = socket.socket()
        s.connect((hostVISServer, portVISClient))

        message = speech
        while True:
            s.send(message.encode('utf-8'))
            Received = s.recv(1024).decode('utf-8')
            #print('Received from server: ' + data)
        s.close()


        self.speech.synthesize_text(Received)

    def __acknowledge_action(self):
        self.__text_action(self.nlg_lite.acknowledge())

    def __text_action(self, text=None):
        if text is not None:
            requests.get("http://localhost:8080/statement?text=%s" % text)
            self.speech.synthesize_text(text)

        def __appearance_action(self):
        requests.get("http://localhost:8080/face")

if __name__ == "__main__":
    main = Main()
    main.start()
