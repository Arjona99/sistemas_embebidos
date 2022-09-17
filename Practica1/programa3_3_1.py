import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

def setupLeds():
  GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)  


def OnOffLeds(state):
  GPIO.output(12, state)
  GPIO.output(16, state)
  GPIO.output(18, state)
  GPIO.output(22, state)
  GPIO.output(24, state)
  GPIO.output(26, state)
  GPIO.output(32, state)


setupLeds()

while True:
  sleep(0.5)
  OnOffLeds(GPIO.HIGH)
  sleep(0.5)
  OnOffLeds(GPIO.LOW)