import RPi.GPIO as GPIO
from time import sleep
from threading import Thread
  
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

sleepTime = 1

flag = True

"""
Programa que configura el GPIO de la Raspberry Pi y mostrar una marquesina rebotando de lado a lado como en efecto ping pong
"""

"""
setupLeds()
Configura los pines 12, 16, 18, 22, 24, 26 y 32 del GPIO como pin de salida
"""
def setupLeds():
  GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)  
  GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW) 
  
   

"""
highOrLow()
@param number número de entrada
@param value  número con el que se compara el parámetro 'number'
@return regresa GPIO.HIGH si la operación number y value son iguales, regresa GPIO.LOW si no lo son
Funcion que evalua dos valores y regresa el valor HIGH o LOW si los valores son iguales
"""
def highOrLow(number, value):
  return GPIO.HIGH if number & value else GPIO.LOW


"""
marquesina()
@param ledEncendido:int número que indica el led encendido
Función que enciende el led correspondiente al parámetro enviado
"""
def marquesina(ledEncendido : int):
  GPIO.output(12, highOrLow(ledEncendido, 0x00000001))
  GPIO.output(16, highOrLow(ledEncendido, 0x00000002))
  GPIO.output(18, highOrLow(ledEncendido, 0x00000004))
  GPIO.output(22, highOrLow(ledEncendido, 0x00000008))
  GPIO.output(24, highOrLow(ledEncendido, 0x00000010))
  GPIO.output(26, highOrLow(ledEncendido, 0x00000020))
  GPIO.output(32, highOrLow(ledEncendido, 0x00000040))
  
def runMarquesina():
    corrNumber = 1
    goingLeft = True
    while True:
        if not flag:
            break 
        sleep(sleepTime)
        marquesina(corrNumber)
        
        if goingLeft:
            corrNumber <<= 1
        else:
            corrNumber >>= 1
            
        if corrNumber == 64 or corrNumber == 1:
            goingLeft = not goingLeft


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
