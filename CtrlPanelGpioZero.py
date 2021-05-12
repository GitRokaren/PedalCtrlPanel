import gpiozero
from gpiozero.output_devices import LED
from gpiozero.input_devices import Button

def main():
    startPin = setInPin(18)
    Pin17 = setInPin(17)
    Pin22 = setInPin(22)
    Pin23 = setOutPin(23)
    Pin24 = setOutPin(24)
    RunPedal(startPin, Pin17, Pin22, Pin23, Pin24)
    
def setOutPin(Nr):
    return LED(Nr)
    
def setInPin(Nr):
    return Button(Nr)

def turnOnOut(LED):
    LED.on()
    
def turnOffOut(LED):
    LED.off()
    
def readIn(Button):
    return int(Button.value)
    
def State0(OutPin1, OutPin2):
    turnOffOut(OutPin1)
    turnOffOut(OutPin2)
    
def State1(OutPin1, OutPin2):
    turnOffOut(OutPin1)
    turnOnOut(OutPin2)
    
def State2(OutPin1, OutPin2):
    turnOnOut(OutPin1)
    turnOffOut(OutPin2)
    
def State3(OutPin1, OutPin2):
    turnOnOut(OutPin1)
    turnOnOut(OutPin2)
    
def checkInput(InPin1, InPin2):
    Check1 = readIn(InPin1)
    Check2 = readIn(InPin2)
    if (Check1 == 1):
        if (Check2 == 1):
            return 0
        else:
            return 1
    else:
        if(Check2 == 1):
            return 2
        else:
            return 3
        
        
def RunPedal(startPin, InPin1, InPin2, OutPin1, OutPin2):
    try:
        while True:
            start = readIn(startPin)
            if (start == 0):
                state = checkInput(InPin1, InPin2)
                if state==0:
                    State0(OutPin1, OutPin2)
                elif state==1:
                    State1(OutPin1, OutPin2)
                elif state==2:
                    State2(OutPin1, OutPin2)
                elif state==3:
                    State3(OutPin1, OutPin2)
                else:
                    print("Error: No input")
            else:
                print("Waiting for established communication")
                
    except KeyboardInterrupt:
            print("DONE")
    
    
if __name__ == "__main__":
    main()

