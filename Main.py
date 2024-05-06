import digitalio
import os
import board

import time
import random
import RPi.GPIO as GPIO
from gpiozero import RGBLED
from gpiozero import Button
from gpiozero import *

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageChops

from adafruit_rgb_display import st7735

# Configuration for CS and DC pins
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)
spi = board.SPI()

# Config for display baudrate
BAUDRATE = 24000000

disp = st7735.ST7735R(
	spi, 
	rotation=90, 
	cs=cs_pin, 
	dc=dc_pin, 
	rst=reset_pin, 
	baudrate=BAUDRATE
	)

#Defines landscape and portrait rotation
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to portrait
    height = disp.height


#Define image object to be referenced
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image
draw.rectangle((0, 0, width, height), fill=(30, 30, 30))
disp.image(image)

GPIO.setmode(GPIO.BCM)

#Define trigger and echo pins
TRIG = 17
ECHO = 27

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

location = (10, 14)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)

draw.rectangle((1, 1, width-1, 28), fill=(0, 0, 0), outline = (150, 150, 150), width = 3)
disp.image(image)

button1 = Button(2)
button2 = Button(3)

redpin = 13
greenpin = 19
bluepin = 26

GPIO.setup(redpin,GPIO.OUT)
GPIO.setup(greenpin,GPIO.OUT)
GPIO.setup(bluepin,GPIO.OUT)

def distanceSensor():
    GPIO.setmode(GPIO.BCM)

    #Define trigger and echo pins
    TRIG = 17
    ECHO = 27

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    #Send a 10*10^-6 s pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    #Look for last time the sensor is 0 and last time it is 1
    while GPIO.input(ECHO) == 0:
	    pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
	    pulse_end = time.time()
	
    #Calculate the pulse duration
    pulse_duration = pulse_end - pulse_start

    #Multiply time * speed of sound / 2 cause its time for wave to go and come back
    distance = pulse_duration * 343 / 2
    distance = round(distance, 2)
    distance = "Distance: " + str(distance) + "m"
    
    #r = random.randint(0, 255)
    #g = random.randint(0, 255)
    #b = random.randint(0, 255)
    draw.rectangle((2, 2, width - 2, 27), fill=(30, 30, 30))
    draw.text(location, distance, font = font, anchor = "lm", fill=(255, 255, 255))
    disp.image(image)
    
    time.sleep(0.001)
 
    disp.image(image)

while True:
    distanceSensor()

"""
def bouncycat():
    #Open image
    image = Image.new("RGB", (width, height))
    image = Image.open("/home/lucas/st7735-python/examples/cat.jpg")

    #Resize the image
    image = image.resize((50,40))
    
    image = ImageChops.offset(image, 100, 100)

    disp.image(image)
"""

 
