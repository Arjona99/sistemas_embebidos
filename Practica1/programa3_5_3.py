import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

def bcd7(num: int):
  GPIO.output(32, GPIO.HIGH if num & 0x00000008 else GPIO.LOW)
  GPIO.output(38, GPIO.HIGH if num & 0x00000004 else GPIO.LOW)
  GPIO.output(40, GPIO.HIGH if num & 0x00000002 else GPIO.LOW)
  GPIO.output(37, GPIO.HIGH if num & 0x00000001 else GPIO.LOW)
  
flag = True
num  = 1
velocidad = int(input("Ingrese la velocidad deseada: "))
while flag:
  try:
    bcd7(num)
    num = num + 1 if (num < 16) else 1
    sleep(velocidad)
  except:
    flag = False
GPIO.cleanup()