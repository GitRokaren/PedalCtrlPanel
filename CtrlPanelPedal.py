import RPi.GPIO as GPIO
from time import sleep

def main():
    activatePins()
    setOutPins()
    setInPins()
    RunPedal()
    
def activatePins():
    GPIO.setmode(GPIO.BCM)
    
def setOutPins():
    GPIO.setup(23,GPIO.OUT)
    GPIO.setup(24,GPIO.OUT)
    GPIO.output(23,0)
    GPIO.output(24,0)
    
def setInPins():
    GPIO.setup(18, GPIO.IN)
    GPIO.setup(17,GPIO.IN)
    GPIO.setup(22,GPIO.IN)
    
def State0():
    GPIO.output(23,0)
    GPIO.output(24,0)
    
def State1():
    GPIO.output(23,0)
    GPIO.output(24,1)
    
def State2():
    GPIO.output(23,1)
    GPIO.output(24,0)
    
def State3():
    GPIO.output(23,1)
    GPIO.output(24,1)
    
def checkInput():
    if ((GPIO.input(17)==False) & (GPIO.input(22)==False)):
        return 0
    elif ((GPIO.input(17)==False) & (GPIO.input(22)==True)):
        return 1
    elif ((GPIO.input(17)==True) & (GPIO.input(22)==False)):
        return 2
    elif ((GPIO.input(17)==True) & (GPIO.input(22)==True)):
        return 3
    else:
        return 4
        
        
def RunPedal():
    try:
        while True:
            if GPIO.input(18):
                state = checkInput()
                if state==0:
                    State0()
                elif state==1:
                    State1()
                elif state==2:
                    State2()
                elif state==3:
                    State3()
                else:
                    print("Error: No input")
            else:
                print("Waiting for established communication")
                
    except KeyboardInterrupt:
            GPIO.cleanup()
    
    
if __name__ == "__main__":
    main()
