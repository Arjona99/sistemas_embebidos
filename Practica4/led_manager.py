# !/usr/bin/env python3
# ## ###############################################
#
# led_manager.py
# Controls leds in the GPIO
#
# Autor: Mauricio Matamoros
# License: MIT
#
# ## ###############################################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# import RPi.GPIO as GPIO
from time import sleep
import threading

# def setupLeds():
#   GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
#   GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
#   GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
#   GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
#   GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
#   GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
#   GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)

SLEEP_TIME = 1.0

def encenderUnLed(ledOn):
    
    print(12 if 0x00000001 & ledOn else 0)
    print(16 if 0x00000002 & ledOn else 0)
    print(18 if 0x00000004 & ledOn else 0)
    print(22 if 0x00000008 & ledOn else 0)
    print(24 if 0x00000010 & ledOn else 0)
    print(26 if 0x00000020 & ledOn else 0)
    print(32 if 0x00000040 & ledOn else 0)
    print('-'*5)
    # GPIO.output(12, if 0x00000001 & ledOn else GPIO.LOW )
    # GPIO.output(16, if 0x00000002 & ledOn else GPIO.LOW )
    # GPIO.output(18, if 0x00000004 & ledOn else GPIO.LOW )
    # GPIO.output(22, if 0x00000008 & ledOn else GPIO.LOW )
    # GPIO.output(24, if 0x00000010 & ledOn else GPIO.LOW )
    # GPIO.output(26, if 0x00000020 & ledOn else GPIO.LOW )
    # GPIO.output(32, if 0x00000040 & ledOn else GPIO.LOW )


""" Enciende el leds especificados en num, apagando los demás
	(To be developed by the student)
"""
def leds(num,stopThreadFlag):
    stopThreadFlag.append('stop')
    print(12 if num == 1 else 0)
    print(16 if num == 2 else 0)
    print(18 if num == 3 else 0)
    print(22 if num == 4 else 0)
    print(24 if num == 5 else 0)
    print(26 if num == 6 else 0)
    print(32 if num == 7 else 0)
    print('-'*5)

    # GPIO.output(12, GPIO.HIGH if num == 1 else GPIO.LOW )
    # GPIO.output(16, GPIO.HIGH if num == 2 else GPIO.LOW )
    # GPIO.output(18, GPIO.HIGH if num == 3 else GPIO.LOW )
    # GPIO.output(22, GPIO.HIGH if num == 4 else GPIO.LOW )
    # GPIO.output(24, GPIO.HIGH if num == 5 else GPIO.LOW )
    # GPIO.output(26, GPIO.HIGH if num == 6 else GPIO.LOW )
    # GPIO.output(32, GPIO.HIGH if num == 7 else GPIO.LOW )
    
    
""" Activa el modo marquesina
	type toma tres valores: left, right y pingpong
	(To be developed by the student)
"""
def marquee(type='pingpong', stopThreadFlag=[]):
    switcher = {
        'left': _marquee_left,
        'right': _marquee_right,
        'pingpong': _marquee_pingpong
    }
    func = switcher.get(type, None)
    if func:
        stopThreadFlag.clear()
        t1 = threading.Thread(target=func, args=(stopThreadFlag,))
        t1.start()


"""	Despliega en número proporcionado en el display de siete segmentos.
	(To be developed by the student)
"""
def bcd(num, stopThreadFlag:list):
    stopThreadFlag.append('stop')
    print(32 if num & 0x0000008 else 0)
    print(38 if num & 0x0000004 else 0)
    print(40 if num & 0x0000002 else 0)
    print(37 if num & 0x0000001 else 0)
    return "BCD jeje"


""" Activa el modo marquesina continua a la izquierda"""
def _marquee_left(stopThreadFlag):
    
    ledOn = 1
    while True:
        encenderUnLed(ledOn)
        ledOn <<= 1
        sleep(SLEEP_TIME)
        if ledOn == 0x00000080:
            ledOn = 1
        if len(stopThreadFlag):
            break


""" Activa el modo marquesina continua a la derecha"""
def _marquee_right(stopThreadFlag):
    
    ledOn = 0x00000040
    while True:
        encenderUnLed(ledOn)
        sleep(SLEEP_TIME)
        ledOn >>= 1
        if ledOn == 0x0000000:
            ledOn = 0x00000040
        if len(stopThreadFlag):
            break



""" Activa el modo marquesina ping-pong"""
def _marquee_pingpong(stopThreadFlag):
    
    ledOn = 1
    goingLeft = True
    while True:
        encenderUnLed(ledOn)
        sleep(SLEEP_TIME)
        
        if goingLeft:
            ledOn <<= 1
        else:
            ledOn >>= 1
        if ledOn == 0x00000040 or ledOn == 0x00000001:
            goingLeft = not goingLeft
        if len(stopThreadFlag):
            break
    
