#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Hand.py:	Description of Hand.py"""

__author__ = "Marc Steinebrunner"
__copyright__ = ""
__credits__ = ""
__license__ = ""
__version__ = "0.3"
__email__ = "marc.steinebrunner@gmail.com"
__status__ = "In Progress"

import RPi.GPIO as GPIO
import time
import sys
"""
F1S = Finger 1 Signal Daumen
F2S = Finger 2 Signal Zeigefinger
F3S = Finger 3 Signal Mittelfinger
F4S = Finger 4 Signal Ringfinger
F5S = Finger 5 Signal Kleinerfinger

H1S = Handgelenk 1 Signal Handgelenk

E1S = Ellenbogen 1 Signal Ellenbogen Horizontale
E2S = Ellenbogen 2 Signal Ellenbogen Vertikal

ELM = Elektro Magnet

EMO = Elektro Motor
"""

def SETUP():
    """
    Diese Funktion ist das setup. Hier werden die Pins festgelegt und
    die Servoobjekte erstellt
    """
    # setze Pins für Servos
    pinarray = {'F1S': 22, 'F2S': 31, 'F3S': 32, 'F4S': 37, 'F5S': 38, 'H1S': 40; 'EMO': 29; 'ELM': 33 'E1S': 36; 'E2S': 35}
    # Beschreibung der Pin-Nummern deklarieren
    GPIO.setmode(GPIO.BOARD)
    # warnungen ausschalten
    GPIO.setwarnings(False)
    # deklariere Pins als Output
    GPIO.setup(pinarray['F1S'], GPIO.OUT)
    GPIO.setup(pinarray['F2S'], GPIO.OUT)
    GPIO.setup(pinarray['F3S'], GPIO.OUT)
    GPIO.setup(pinarray['F4S'], GPIO.OUT)
    GPIO.setup(pinarray['F5S'], GPIO.OUT)

    GIPO.setup(pinarray['H1S'], GPIO.OUT)
    #GIPO.setup(pinarray['EMO'], GPIO.OUT)
    #GIPO.setup(pinarray['ELM'], GPIO.OUT)

    GPIO.setup(pinarray['E1S'], GPIO.OUT)
    GPIO.setup(pinarray['E2S'], GPIO.OUT)

    # Servoobjekte erstellen
    Servo_F1S = GPIO.PWM(pinarray['F1S'], 50)
    Servo_F2S = GPIO.PWM(pinarray['F2S'], 50)
    Servo_F3S = GPIO.PWM(pinarray['F3S'], 50)
    Servo_F4S = GPIO.PWM(pinarray['F4S'], 50)
    Servo_F5S = GPIO.PWM(pinarray['F5S'], 50)

    Servo_H1S = GPIO.PWM(pinarray['H1S'], 50)

    Servo_E1S = GPIO.PWM(pinarray['E1S'], 50)
    Servo_E2S = GPIO.PWM(pinarray['E2S'], 50)

    Magnet_EML = GIPO.setup(pinarray['ELM'], GPIO.OUT)
    Motor_EMO  = GIPO.setup(pinarray['EMO'], GPIO.OUT)
    # Objekte übergeben
    return Servo_F1S, Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S, Servo_H1S, Magnet_EML, Motor_EMO, Servo_E1S, Servo_E2S


def STARTPOSITIONING(Servo_F1S, Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S, Servo_H1S, Magnet_EML, Motor_EMO, Servo_E1S, Servo_E2S):
    """
    Funktion zur Ansteuerung der Startpositionen der Servos
    """
    for on in Servo_F1S, Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S:
        on.start(12.5)

    for n in Servo_H1S:
        n.start(7.5)

    for off in Servo_E1S, Servo_E2S;
        off.start(2.5)

    GPIO.output(Motor_EMO,GPIO.LOW);
    GPIO.output(Magnet_EML,GPIO.LOW);

def TOSTART(Servo_F1S, Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S, Servo_H1S, Magnet_EML, Motor_EMO, Servo_E1S, Servo_E2S):
    Servo_F1S.ChangeDutyCycle(12.5)
    Servo_F2S.ChangeDutyCycle(12.5)
    Servo_F3S.ChangeDutyCycle(12.5)
    Servo_F4S.ChangeDutyCycle(12.5)
    Servo_F5S.ChangeDutyCycle(12.5)

    Servo_H1S.ChangeDutyCycle(7.5)

    Servo_E1S_ChangeDutyCycle(2.5)
    Servo_E2S_ChangeDutyCycle(7.5)

    GPIO.output(Motor_EMO,GPIO.LOW)
    GPIO.output(Magnet_EML,GPIO.LOW)

def F1ROTATE(Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S):
    """
    Aus Technischen Gründen konnten wir den daumen nicht in den Programm snippet implientieren.
    """
    Servo_F5S.ChangeDutyCycle(2.5)
    time.sleep(2)
    Servo_F5S.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    Servo_F4S.ChangeDutyCycle(2.5)
    time.sleep(2)
    Servo_F4S.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    Servo_F3S.ChangeDutyCycle(2.5)
    time.sleep(2)
    Servo_F3S.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    Servo_F2S.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    Servo_F2S.ChangeDutyCycle(12.5)

def GLUEBIRNE(Servo_F1S, Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S, Servo_H1S, Magnet_EML, Motor_EMO, Servo_E1S, Servo_E2S):
    t = 100;
    E2S.ChangeDutyCycle(12.5)
    time.sleep(2)
    GPIO.output(Magnet_EML,GPIO.HIGH)
    Eingabe = input("Start = 1 ")
        if int(Eingabe) == 1:
            E2S.ChangeDutyCycle(7.5)
            H1S.ChangeDutyCycle(12.5)
            Eingabe1 = input("Bereit für Fassung ")
                if int(Eingabe1) == 1:
                    GPIO.output(Motor_EMO,GPIO.HIGH);
                    time.sleep(t)
                    GPIO.output(Motor_EMO,GPIO.LOW);
                    GPIO.output(Magnet_EML,GPIO.LOW);
                    break
                else
                    print("Falsche Eingabe !")
                    break
        else
            print("Falsche Eingabe !")
            break

        TOSTART(Servo_F1S, Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S, Servo_H1S, Magnet_EML, Motor_EMO, Servo_E1S, Servo_E2S)

def F2ROTATE(Servo_F1S, Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S, Servo_H1S, Servo_E1S):
    Servo_E1S.ChangeDutyCycle(7.5)
    Servo_H1S.ChangeDutyCycle(2.5)
    time.sleep(2)
    Servo_H1S.ChangeDutyCycle(7.5)
    for i in Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S:
        i.ChangeDutyCycle(2.5)
    time.sleep(1.5)
    Servo_F1S.ChangeDutyCycle(2.5)
    time.sleep(5)
    Servo_F1S.ChangeDutyCycle(12.5)
    time.sleep(1.5)
    for x in Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S:
        x.ChangeDutyCycle(12.5)

def ACTION1(Servo_F1S, Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S, Servo_H1S, Servo_E1S, Servo_E2S):
    try:
        Servo_E1S.ChangeDutyCycle(7.5)

        while x < 5:
            F1rotate()
            x+1
        tostart()

    except KeyboardInterrupt:
        print("stopping Process, exit to main-menue")
        return


def ACTION2(Servo_F1S, Servo_F2S, Servo_F3S, Servo_F4S, Servo_F5S, Servo_H1S, Servo_E1S):
    try:

            F2ROTATE()
            TOSTART()

            except KeyboardInterrupt:
            print("stopping Process, exit to main-menue")
            return



def ACTION3(Servo_ZF, Servo_MF, Servo_RF, Servo_KF):
    try:
        while True:
            print("für den Daumen 1, für Zeigefinger 2, für Mittelfinger 3, für Ringfinger 4, für den Kleinerfinger die 5, für das Handgelenk 6, für den Ellenbogen1 7, für den Ellenbogen2 8")
            Eingabe1 = input("Bitte eingeben welcher Finger sich bewegen soll:")

            # Kontrolle ob die Eingabe eine Zahl ist.
            if Eingabe1.isdigit():
                Zahl = int(Eingabe1)

                if Zahl == 1:
                    Servo_F1S.ChangeDutyCycle(0.5)
                    time.sleep(2)
                    Servo_F1S.ChangeDutyCycle(2.5)
                    sys.exit(0)
                    break
                elif Zahl == 2:
                    Servo_F2S.ChangeDutyCycle(0.5)
                    time.sleep(2)
                    Servo_F2S.ChangeDutyCycle(2.5)
                    sys.exit(0)
                    break
                elif Zahl == 3:
                    Servo_F3S.ChangeDutyCycle(0.5)
                    time.sleep(2)
                    Servo_F3S.ChangeDutyCycle(2.5)
                    sys.exit(0)
                    break
                elif Zahl == 4:
                    Servo_F4S.ChangeDutyCycle(2.5)
                    time.sleep(2)
                    Servo_F4S.ChangeDutyCycle(7.5)
                    sys.exit(0)
                    break
                elif Zahl == 5:
                    Servo_F5S.ChangeDutyCycle(2.5)
                    time.sleep(2)
                    Servo_F5S.ChangeDutyCycle(7.5)
                    sys.exit(0)
                    break
                elif Zahl == 6:
                    Servo_H1S.ChangeDutyCycle(2.5)
                    time.sleep(2)
                    Servo_E2S.ChangeDutyCycle(7.5)
                    time.sleep(0.5)
                    Servo_H1S.ChangeDutyCycle(12.5)
                    time.sleep(2)
                    Servo_H1S.ChangeDutyCycle(7.5)
                    sys.exit(0)
                    break
                elif Zahl == 7:
                    Servo_E1S.ChangeDutyCycle(2.5)
                    time.sleep(2)
                    Servo_E1S.ChangeDutyCycle(7.5)
                    sys.exit(0)
                    break
                elif Zahl == 8:
                    Servo_E2S.ChangeDutyCycle(2.5)
                    time.sleep(2)
                    Servo_E2S.ChangeDutyCycle(7.5)
                    time.sleep(0.5)
                    Servo_E2S.ChangeDutyCycle(12.5)
                    time.sleep(2)
                    Servo_E2S.ChangeDutyCycle(7.5)
                    sys.exit(0)
                    break

                elif Zahl > 8:
                    print("Falsche Eingabe bitte überprüfen")
                    break
            else:
                print("It was at least a wrong number entered")
                sys.exit(1)
    except KeyboardInterrupt:
            print("stopping Process, exit...")
            sys.exit(0)



def main():
    welcomestring = "       ***Robot-Hand-Controller***\n" \
                    "          by Marc Steinebrunner\n\n"
    print(welcomestring)
    Servo_ZF, Servo_MF, Servo_RF, Servo_KF = setup()
    STARTPOSITIONING(Servo_ZF, Servo_MF, Servo_RF, Servo_KF)
    while True:
        Eingabe = input("Wählen sie eine der Möglichkeiten(1,2,3): ")
        if int(Eingabe) == 1:
            ACTION1(Servo_ZF, Servo_MF, Servo_RF, Servo_KF)
        elif int(Eingabe) == 2:
            ACTION2(Servo_ZF, Servo_MF, Servo_RF, Servo_KF)
        elif int(Eingabe)== 3:
            ACTION3(Servo_ZF, Servo_MF, Servo_RF, Servo_KF)
        elif str(Eingabe) == "exit":
            break
        else:
            continue
    return

if __name__ == '__main__':
    Main()
    sys.exit(0)
