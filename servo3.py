import time

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c)
pca.frequency = 50
servo1 = servo.Servo(pca.channels[0])
servo2 = servo.Servo(pca.channels[1])

while True:
    servo1.angle = 90
    servo2.angle = 90
    time.sleep(2)
    servo1.angle = 0
    servo2.angle = 0
    time.sleep(2)
    servo1.angle = 90
    servo2.angle = 90
    time.sleep(2)
    servo1.angle = 180
    servo2.angle = 180
    time.sleep(2)

#for i in range(90):
    #servo7.angle = i
    #time.sleep(0.01)
#for i in range(270):
    #servo7.angle = i
    #time.sleep(0.01)
#for i in range(135):
    #servo7.angle = 270 - i
    #time.sleep(0.01)


pca.deinit()
