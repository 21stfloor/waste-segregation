import board
import busio
from adafruit_pca9685 import PCA9685
import time
from adafruit_motor import servo

# Initialize the I2C bus and PCA9685 object
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)

# Set the PWM frequency (usually 50Hz for servos)
pca.frequency = 50

# Set the channel numbers for your two servos
servo_channel_1 = 0  # First servo
servo_channel_2 = 1  # Second servo

# Define pulse width values for your servos (adjust as needed)
# These values correspond to the servo's full range of motion
servo_min = 150  # Minimum pulse width (for 0 degrees)
servo_max = 600  # Maximum pulse width (for 180 degrees)

# Function to move two servos to the same angle
def move_servos(angle):
    angle = max(0, min(180, angle))  # Ensure angle is within valid range (0-180)
    pulse_width = int(servo_min + (angle / 180) * (servo_max - servo_min))        
    pca.channels[servo_channel_1].duty_cycle = int(pulse_width * 4096 / 1000)
    pca.channels[servo_channel_2].duty_cycle = int(pulse_width * 4096 / 1000)


def set_servo_angle(channel, angle):
    angle = max(0, min(180, angle))  # Ensure angle is within valid range (0-180)
    pulse_length = int(servo_min + (angle / 180) * (servo_max - servo_min))
    pca.channels[channel].duty_cycle = int(pulse_length * 4096 / 1000)

servo1 = servo.Servo(pca.channels[0])
servo2 = servo.Servo(pca.channels[1])

servo3 = servo.Servo(pca.channels[3])
servo4 = servo.Servo(pca.channels[2])


def return_wood1():
    print('servo3.angle:  =  ' + str(servo3.angle))
    print('servo4.angle:  =  ' + str(servo4.angle))
    if servo3.angle is None:
        pass
    # elif servo3.angle < 72 and servo3.angle > 68:
        # pass
        # time.sleep(2)
    else:
        angle = servo3.angle
        print('angle:  =  ' + str(angle))
        for i in range(0, 70, 2):
            if servo3.angle < 72 and servo3.angle > 68:
                #servo3.angle = 70
                #servo4.angle = 70
                pass
            # servo3.angle = 140 - i
            # servo4.angle = i

def drop_wood1():
    print('drop wood1')
    
    for i in range(90):        
        servo3.angle = 90 - i
        servo4.angle = 90 + i
    time.sleep(1)
    
def drop_wood2_left():
    
    
    print('into: 180')
    for i in range(90):
        servo1.angle = 90 + i
        servo2.angle = 90 - i 
    time.sleep(1)
    
    print('into: 90')
    #rotate back to mid
    for i in range(90):
        servo1.angle = 180 - i
        servo2.angle = i
    time.sleep(1)
    
    
def drop_wood2_right():
    
    for i in range(90):
        servo1.angle = 180 - i
        servo2.angle = i
    time.sleep(1)
    
    print('into: 0')
    for i in range(90):
        servo1.angle = 90 - i
        servo2.angle = 90 + i
    time.sleep(1)

    
    
def return_wood2_right():
    print('into: 90')
    for i in range(90):
        servo1.angle = i
        servo2.angle = 180 - i
    time.sleep(1)


def return_wood2_left():
    print('into: 90')
    for i in range(90):
        servo1.angle = i
        servo2.angle = 180 - i
        
    time.sleep(1)



def drop_woods_left():
    
    
    print('into: 180')
    for i in range(0, 70, 2):
        servo1.angle = 70 + i
        servo2.angle = 70 - i 
        
        servo3.angle = 70 - i
        servo4.angle = 70 + i
    time.sleep(1)
    
    print('into: 90')
    #rotate back to mid
    for i in range(0, 70, 2):
        servo1.angle = 140 - i
        servo2.angle = i
        
        # if servo3.angle < 91 and servo3.angle > 89:
            # pass
        servo3.angle = 140 - i
        servo4.angle = i
    time.sleep(1)
    
    
def drop_woods_right():
    
    for i in range(0, 70, 2):
        servo1.angle = 70 - i
        servo2.angle = 70 + i
        
        servo3.angle = 70 - i
        servo4.angle = 70 + i
    time.sleep(1)
    
    print('into: 0')
    for i in range(0, 70, 2):
        servo1.angle = i
        servo2.angle = 140 - i
        
        # if servo3.angle < 91 and servo3.angle > 89:
            # pass
        servo3.angle = 140 - i
        servo4.angle = i
    time.sleep(1)
    
def reset_all():
	servo1.angle = 0
	servo2.angle = 0
	servo3.angle = 0
	servo4.angle = 0
