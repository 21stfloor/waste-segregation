import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for Red, Green, and Blue for each LED
led_pins = {
    "LED1": (17, 27, 22),
    "LED2": (5, 6, 13),
    "LED3": (19, 26, 18),
    "LED4": (23, 24, 25),
    "LED5": (12, 16, 20),
    "LED6": (21, None, None)  # Note: Some pins can be shared for GND or VCC
}

# Set up the GPIO pins as output
for led, (red_pin, green_pin, blue_pin) in led_pins.items():
    if red_pin is not None:
        GPIO.setup(red_pin, GPIO.OUT)
    if green_pin is not None:
        GPIO.setup(green_pin, GPIO.OUT)
    if blue_pin is not None:
        GPIO.setup(blue_pin, GPIO.OUT)

# Function to set the color for a specific LED
def set_color(led, red, green, blue):
    red_pin, green_pin, blue_pin = led_pins[led]
    if red_pin is not None:
        GPIO.output(red_pin, red)
    if green_pin is not None:
        GPIO.output(green_pin, green)
    if blue_pin is not None:
        GPIO.output(blue_pin, blue)

# List of colors in RGB format (Red, Green, Blue)
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]  # Red, Green, Blue

try:
    while True:
        for led in led_pins:
            for color in colors:
                set_color(led, *color)
                time.sleep(1)  # Change color every 1 second

except KeyboardInterrupt:
    pass

# Cleanup and exit
GPIO.cleanup()
