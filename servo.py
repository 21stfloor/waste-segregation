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
# while True:
    # # Move the servo to 0 degrees
    # set_servo_angle(servo_channel_1, 0)
    # time.sleep(3)
    # pca.channels[servo_channel_1].angle = 90
    # # Move the servo to 90 degrees
    # set_servo_angle(servo_channel_1, 90)
    # time.sleep(3)
    
    # # Move the servo to 180 degrees
    # set_servo_angle(servo_channel_1, 180)
    # time.sleep(3)
while True:
    #rotate back to mid
    print('into: 90')
    for i in range(90):
        servo1.angle = i
        servo2.angle = 180 - i
        time.sleep(0.01)
    time.sleep(1)
    
    print('into: 180')
    for i in range(90):
        servo1.angle = 90 + i
        servo2.angle = 90 - i 
        time.sleep(0.01)
    time.sleep(1)
    print('into: 90')
    #rotate back to mid
    for i in range(90):
        servo1.angle = 180 - i
        servo2.angle = i
        time.sleep(0.01)
    time.sleep(1)
    print('into: 0')
    
    for i in range(90):
        servo1.angle = 90 - i
        servo2.angle = 90 + i
        time.sleep(0.01)
    time.sleep(1)

