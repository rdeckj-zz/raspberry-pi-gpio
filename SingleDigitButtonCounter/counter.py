from gpiozero import LED, Button
from time import sleep
from signal import pause

button = Button(2)

segA = LED(14)
segB = LED(15)
segC = LED(18)
segD = LED(23)
segE = LED(24)
segF = LED(25)
segG = LED(8)

currentNumber = 0

def zero():
    segA.on()
    segB.on()
    segC.on()
    segD.on()
    segE.on()
    segF.on()
    segG.off()

def one():
    segA.off()
    segB.on()
    segC.on()
    segD.off()
    segE.off()
    segF.off()
    segG.off()

def two():
    segA.on()
    segB.on()
    segC.off()
    segD.on()
    segE.on()
    segF.off()
    segG.on()

def three():
    segA.on()
    segB.on()
    segC.on()
    segD.on()
    segE.off()
    segF.off()
    segG.on()

def four():
    segA.off()
    segB.on()
    segC.on()
    segD.off()
    segE.off()
    segF.on()
    segG.on()
    
def five():
    segA.on()
    segB.off()
    segC.on()
    segD.on()
    segE.off()
    segF.on()
    segG.on()
    
def six():
    segA.on()
    segB.off()
    segC.on()
    segD.on()
    segE.on()
    segF.on()
    segG.on()
    
def seven():
    segA.on()
    segB.on()
    segC.on()
    segD.off()
    segE.off()
    segF.off()
    segG.off()
    
def eight():
    segA.on()
    segB.on()
    segC.on()
    segD.on()
    segE.on()
    segF.on()
    segG.on()
    
def nine():
    segA.on()
    segB.on()
    segC.on()
    segD.off()
    segE.off()
    segF.on()
    segG.on()

digits = {0 : zero,
          1 : one,
          2 : two,
          3 : three,
          4 : four,
          5 : five,
          6 : six,
          7 : seven,
          8 : eight,
          9 : nine
}

def increment():
    global currentNumber
    if currentNumber == 9:
        currentNumber = 0
    else:
        currentNumber = currentNumber + 1
        
    digits[currentNumber]()

zero()
button.when_released = increment

pause()
