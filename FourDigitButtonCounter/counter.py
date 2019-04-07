from gpiozero import LED, Button
from time import sleep
from signal import pause
from threading import Thread

usleep = lambda x: sleep(x/1000000.0)

button = Button(22)

segA = LED(12)
segB = LED(1)
segC = LED(19)
segD = LED(13)
segE = LED(6)
segF = LED(7)
segG = LED(5)
segDP = LED(0)

dig1 = LED(16)
dig2 = LED(20)
dig3 = LED(21)
dig4 = LED(26)

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

def initialize():
    enableDigit(4)
    zero()

numbers = {0 : zero,
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
 
def enableDigit(digit):
    if digit == 1:
        dig1.off()
        dig2.on()
        dig3.on()
        dig4.on()
    if digit == 2:
        dig1.on()
        dig2.off()
        dig3.on()
        dig4.on()
    if digit == 3:
        dig1.on()
        dig2.on()
        dig3.off()
        dig4.on()
    if digit == 4:
        dig1.on()
        dig2.on()
        dig3.on()
        dig4.off()

def display(number):
    displayString = str(number)
    if number < 10:
        numbers[number]()
    if number >= 10:
        enableDigit(3)
        numbers[int(displayString[0])]()
        usleep(5000)
        enableDigit(4)
        numbers[int(displayString[1])]()    
	usleep(5000)
    if number >= 100:
        enableDigit(2)
        numbers[int(displayString[0])]()
        usleep(5000)
        enableDigit(3)
        numbers[int(displayString[1])]()
        usleep(5000)
        enableDigit(4)
        numbers[int(displayString[2])]()    
	usleep(5000)
 
def increment():
    global currentNumber
    if currentNumber == 9999:
        currentNumber = 0
    else:
        currentNumber = currentNumber + 1
        
def incrementTask(args):
    button.when_released = increment

def displayTask(args):
    global currentNumber
    while True:
        display(currentNumber)

initialize()
tasks = [incrementTask, displayTask]
data = "something"
for task in tasks:
    t = Thread(target=task, args=(data,))
    t.start()

pause()
