import pigpio

class Robot:
    pins = {
        'leftMotor1' : 17,
        'leftMotor2' : 18,
        'leftMotorPWM' : 12,
        'rightMotor1' : 5,
        'rightMotor2' : 6,
        'rightMotorPWM' : 13,
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
    def __init__(self, pi: pigpio.pi, input1GPIONumber: int, input2GPIONumber: int, pwmGPIONumber: int):
        self.pi = pi
        self.input1 = input1GPIONumber
        self.input2 = input2GPIONumber
        self.PWM = pwmGPIONumber
