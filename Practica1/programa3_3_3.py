import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

sleepTime = 1
flag = True

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
  GPIO.output(32, highOrLow(ledEncendido, 0x00000001))
  GPIO.output(26, highOrLow(ledEncendido, 0x00000002))
  GPIO.output(24, highOrLow(ledEncendido, 0x00000004))
  GPIO.output(22, highOrLow(ledEncendido, 0x00000008))
  GPIO.output(18, highOrLow(ledEncendido, 0x00000010))
  GPIO.output(16, highOrLow(ledEncendido, 0x00000020))
  GPIO.output(12, highOrLow(ledEncendido, 0x00000040))
  
def runMarquesina():
    corrNumber = 1
    while True:
        if not flag:
            break 
        sleep(sleepTime)
        marquesina(corrNumber)
        corrNumber <<= 1
        if corrNumber == 128:
            corrNumber = 1


setupLeds()
thread1 = Thread(target=runMarquesina)
thread1.start()


while flag:
    try:        
        rpm = int(input("Ingrese la velocidad deseada (rpm): "))
        sleepTime = (60 / 7) / rpm
    except:
        flag = False
        thread1.join()

GPIO.cleanup()