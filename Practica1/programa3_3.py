import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)

while True:
  sleep(0.5)
  GPIO.output(32, GPIO.HIGH)
  sleep(0.5)
  GPIO.output(32, GPIO.LOW)