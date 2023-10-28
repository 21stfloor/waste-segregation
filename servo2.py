import board
import busio
from adafruit_pca9685 import PCA9685
import time

# Initialize the I2C bus and PCA9685 object
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)

# Set the PWM frequency (usually 50Hz for servos)
pca.frequency = 50

# Set the channel number for your servo (0 to 15)
servo_channel = 0

# Define pulse width values for your servo (adjust as needed)
# These values correspond to the servo's full range of motion
servo_min = 150  # Minimum pulse width (for 0 degrees)
servo_max = 600  # Maximum pulse width (for 180 degrees)

# Function to move the servo to a specific angle
def move_servo(angle):
    angle = max(0, min(180, angle))  # Ensure angle is within valid range (0-180)
    pulse_width = int(servo_min + (angle / 180) * (servo_max - servo_min))
    pca.channels[servo_channel].duty_cycle = int(pulse_width * 4096 / 1000)

# Move the servo to its minimum position (0 degrees)
move_servo(0)
time.sleep(1)

# Move the servo to its maximum position (180 degrees)
move_servo(180)
time.sleep(1)

# Move the servo back to the center position (90 degrees)
move_servo(90)
time.sleep(1)

while True:  
    for i in range(90):
        servo1.angle = i
        servo2.angle = i
        time.sleep(0.01)
    time.sleep(1)
    for i in range(90):
        servo1.angle = 90+i
        servo2.angle = 90+i
        time.sleep(0.01)
    time.sleep(1)
    for i in range(90):
        servo1.angle = 180-i
        servo2.angle = 180-i
        time.sleep(0.01)
    time.sleep(1)
    for i in range(90):
        servo1.angle = 90-i
        servo2.angle = 90-i
        time.sleep(0.01)
    time.sleep(1)
