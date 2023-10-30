import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for Red, Green, and Blue
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

# Set up the GPIO pins as output
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Function to set the color
def set_color(red, green, blue):
    GPIO.output(RED_PIN, red)
    GPIO.output(GREEN_PIN, green)
    GPIO.output(BLUE_PIN, blue)

# Example: Turn on the Red color
set_color(1, 0, 0)

# You can create other color combinations by calling the set_color function.

# Cleanup and exit
GPIO.cleanup()
