import os
import time
import RPi.GPIO as GPIO
#------------------- Used Pins asignation ---------------
PinMS1 = 2                  # Output, MS1 (Mode ), pin number 3
PinMS2 = 3                  # Output, MS2 (Mode ), pin number 5
PinMS3 = 14                 # Output, MS3 (Mode ), pin number 8
PinStep = 4                 # Output, Step (Pulses), pin number 7
PinDir = 15                 # Output, Dir (Direction), pin number 10
PinFdCWhite = 18                    # Input, LimitDetector 1 White, pin number 12
PinFdCYellow = 17                    # Input, LimitDetector 2 Yellow, pin number 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(PinMS1, GPIO.OUT)
GPIO.setup(PinMS2, GPIO.OUT)
GPIO.setup(PinMS3, GPIO.OUT)
GPIO.setup(PinDir, GPIO.OUT)
GPIO.setup(PinStep, GPIO.OUT)
GPIO.setup(PinFdCWhite, GPIO.IN)
GPIO.setup(PinFdCYellow, GPIO.IN)
os.system('clear')

def ShowValues():
    pass


def ConfigModeSpeed():
    pass


def SetModeSpeed():
    pass


def ConfigDirection():
    pass


def SetDirection():
    pass


def GoLimit():
    pass

def ConfigSteps():
    pass


def SetSteps():
    pass


# ============================================================================
# ============================= MAIN =========================================
# ============================================================================
exit = False                           # Initial Values
vMS = 1                                 # value MS (1, 2, 4, 8, 16)
vDir = 1                                # value Dir: 1 (to White) , 2 (to Yellow)
vSteps = 0                              # value vSteps (1, ...)
GPIO.output(PinStep, GPIO.LOW)          # always initialitzed at '0'
SetModeSpeed()
SetDirection()
vLDWhite = GPIO.input(PinFdCWhite)
vLDYellow = GPIO.input(PinFdCYellow)
steps = 0                               # running steps

while not exit:
    print ('Options:')
    print ('    E.- Exit program ')
    print ('    M.- Speed Mode ')
    print ('    D.- Direction ')
    print ('    L.- Go to Limit ')
    print ('    S.- Go to Steps ')
    print ("-------------------------------------------------------------------------")
    print
    ShowValues()
    print ("-------------------------------------------------------------------------")
    print
    op = input('> ')
    if (op == "E" or op == "e"):
        pass

    if (op == "M" or op== "m"):
        pass

    if (op == "D" or op== "d"):
        pass

    if (op == "L" or op == "l"):
        pass

    if (op == "S" or op == "s"):
        exit = True

# ---------------------------------------------------------------
GPIO.cleanup()
# ---------------------------------------------------------------