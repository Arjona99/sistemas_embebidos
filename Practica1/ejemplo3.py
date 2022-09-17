import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW) # A
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW) # B
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW) # C
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW) # D

def bcd7(num):
    GPIO.output(36, GPIO.HIGH if num & 0x00000008 else GPIO.LOW)
    GPIO.output(38, GPIO.HIGH if num & 0x00000004 else GPIO.LOW)
    GPIO.output(40, GPIO.HIGH if num & 0x00000002 else GPIO.LOW)
    GPIO.output(37, GPIO.HIGH if num & 0x00000001 else GPIO.LOW)

flag = True
while flag:
    try:
        num = int(input("Ingrese número entero: "))
        bcd7(num)
    except:
        flag = False
        
GPIO.cleanup()
    
    
    