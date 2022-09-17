import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(32,GPIO.OUT, initial=GPIO.LOW)

pwm = GPIO.PWM(32,100)

pwm.start(0)
flag = True
while flag:
  try:
    
    for i in range(0,101):
        pwm.ChangeDutyCycle(i)
        sleep(1/100)
    sleep(0.5)
    for i in range(100,-1,-1):
        pwm.ChangeDutyCycle(i)
        sleep(1/100)
  except:
    flag = False
    pwm.ChangeDutyCycle(0)
    
pwm.stop()

GPIO.cleanup()
