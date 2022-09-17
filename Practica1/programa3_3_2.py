import RPi.GPIO as GPIO
from time import sleep



def setupLeds():
  GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)  

def highOrLow(number, value):
  return GPIO.HIGH if number & value else GPIO.LOW

def marquesina(ledEncendido : int):
  GPIO.output(12, highOrLow(ledEncendido, 0x00000001))
  GPIO.output(16, highOrLow(ledEncendido, 0x00000002))
  GPIO.output(18, highOrLow(ledEncendido, 0x00000004))
  GPIO.output(22, highOrLow(ledEncendido, 0x00000008))
  GPIO.output(24, highOrLow(ledEncendido, 0x00000010))
  GPIO.output(26, highOrLow(ledEncendido, 0x00000020))
  GPIO.output(32, highOrLow(ledEncendido, 0x00000040))
  
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

setupLeds()

corrNumber = 1

while True:
  sleep(0.5)
  marquesina(corrNumber)
  corrNumber <<= 1
  if corrNumber == 128:
    corrNumber = 1
  