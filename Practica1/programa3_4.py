import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(32,GPIO.OUT, initial=GPIO.LOW)

pwm = GPIO.PWM(32,1)

pwm.start(50)
flag = True
while flag:
  try:
    dutyCycle = int(input("Ingrese ciclo de trabajo: "))
    pwm.ChangeDutyCycle(dutyCycle)
  except:
    flag = False
    pwm.ChangeDutyCycle(0)
    
pwm.stop()

GPIO.cleanup()