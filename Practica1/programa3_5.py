import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
PINS = [12,16,18,22,24,26,32]

def setupLeds():
  GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
  
def getNum(num: int):
  bcdDict = {
    #   abcdefg
    0: '1111110',
    1: '0110000',
    2: '1101101',
    3: '1111001',
    4: '0110011',
    5: '1011011',
    6: '1011111',
    7: '1110000',
    8: '1111111',
    9: '1111011'
  }
  return(bcdDict.get(num))

  
"""
PIN TO SEGMENT MAP
a 12
b 16
c 18
d 22
e 24
f 26
g 32
"""
def bcd7(num: int):
  bcdNum = getNum(num)
  for index in range(len(bcdNum)):
    GPIO.output(PINS[index], GPIO.HIGH if(bcdNum[index] == '1') else GPIO.LOW)
  
  
setupLeds()  
flag = True
while flag:
  try:
    num = int(input("Ingrese número entero: "))
    bcd7(num)
  except:
    flag = False
GPIO.cleanup()