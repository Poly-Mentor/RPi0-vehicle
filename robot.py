import pigpio
from math import floor
from time import sleep

class Robot:
    pins = {
        'rightMotor1' : 17,
        'rightMotor2' : 27,
        'rightMotorPWM' : 12,
        'leftMotor1' : 5,
        'leftMotor2' : 6,
        'leftMotorPWM' : 13,
        'LED1' : 23,
        'LED2' : 24,
        'servo1' : 18,
        'servo2' : 19,
        'MOSFET1' : 25,
        'MOSFET2' : 26
    }

    def __init__(self):
        self.pi = pigpio.pi()
        self.LED1 = LED(self.pi, self.pins['LED1'])
        self.LED2 = LED(self.pi, self.pins['LED2'])
        self.leftMotor = Motor(self.pi, self.pins["leftMotor1"], self.pins["leftMotor2"], self.pins["leftMotorPWM"], invert=True)
        self.rightMotor = Motor(self.pi, self.pins["rightMotor1"], self.pins["rightMotor2"], self.pins["rightMotorPWM"])
    
    def drive(self, x: int, y: int):
        if (x > 100 or y > 100 or x < -100 or y < -100):
            raise ValueError
        if y > 49 or y < -49 or y == 0:
            leftMV = rightMV = y
        elif y > 0 and y <= 49:
            leftMV = rightMV = 50
        elif y < 0 and y >= -49:
            leftMV = rightMV = -50
        
        if x >= 0:
            if y >= 0:
                if abs(y) > 65:
                    rightMV -= floor(x/2)
                else:
                    rightMV = 0
            if y < 0:
                if abs(y) > 65:
                    rightMV += floor(x/2)
                else:
                    rightMV = 0
        else:
            if y >= 0:
                if abs(y) > 65:
                    leftMV -= floor(x/2)
                else:
                    leftMV = 0
            if y < 0:
                if abs(y) > 65:
                    leftMV += floor(x/2)
                else:
                    leftMV = 0
        print("Motors MVs: %s, %s" % (leftMV, rightMV))
        self.leftMotor.mv(leftMV)
        self.rightMotor.mv(rightMV)
    
    def run(self):
        for speed in range(100):
            self.leftMotor.mv(speed)
            self.rightMotor.mv(speed)
            sleep(0.01)
        for speed in range(100, 0, -1):
            self.leftMotor.mv(speed)
            self.rightMotor.mv(speed)
            sleep(0.01)


class LED:
    def __init__(self, pi: pigpio.pi, GPIO: int):
        self.GPIO = GPIO
        self.pi = pi
        self.pi.set_mode(self.GPIO, pigpio.OUTPUT)
    
    def on(self):
        self.pi.write(self.GPIO, 1)
    
    def off(self):
        self.pi.write(self.GPIO, 0)
        

class Motor:
    def __init__(self, pi: pigpio.pi, input1GPIONumber: int, input2GPIONumber: int, pwmGPIONumber: int, invert=False):
        self.pi = pi
        if not invert:
            self.input1 = input1GPIONumber
            self.input2 = input2GPIONumber
        else:
            self.input2 = input1GPIONumber
            self.input1 = input2GPIONumber 
        self.PWM = pwmGPIONumber
        self.pi.set_mode(self.input1, pigpio.OUTPUT)
        self.pi.set_mode(self.input2, pigpio.OUTPUT)
        self.pi.set_mode(self.PWM, pigpio.OUTPUT)

    def mv(self, mv: int):
        if mv == 0:
            self.pi.write(self.input1, 0)
            self.pi.write(self.input2, 0)
            self.pi.hardware_PWM(self.PWM, 50, 0)
        elif mv < 0:
            self.pi.write(self.input1, 1)
            self.pi.write(self.input2, 0)
            self.pi.hardware_PWM(self.PWM, 50, -mv*10000)
        else:
            self.pi.write(self.input1, 0)
            self.pi.write(self.input2, 1)
            self.pi.hardware_PWM(self.PWM, 50, mv*10000)

