#!/usr/bin/python3
#
# Measure distance using an ultrasonic module
# in a loop and light leds dependant on distance and place blocks in Minecraft.
#
# created for the Brighton Science Festival by Neil C Ford (@neilcford)
# worksheet can be found at https://github.com/NeilCFord/BrightonScienceFestival

# Import required Python libraries

import time
import RPi.GPIO as GPIO
import mcpi.minecraft as minecraft

# Define some functions

def measure():
  # This function measures a distance
  GPIO.output(trigger, True)
  time.sleep(0.00001)
  GPIO.output(trigger, False)
  start = time.time()

  while GPIO.input(echo)==0:
    start = time.time()

  while GPIO.input(echo)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance


def measure_average():
  # This function takes 3 measurements and
  # returns the average.
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

# Main Script

# Use BCM GPIO references instead of physical pin numbers.
# Also set warnings to False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO to use on Pi
trigger = 16
echo = 20
redled = 11
yellowled = 9
greenled = 10

# create CONSTANTS for block and light colours
AIR = 0
STONE = 1
WOOL = 35
BLACK = 15
RED = 14
YELLOW = 4
GREEN = 5

print ("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(trigger,GPIO.OUT)    # Trigger
GPIO.setup(echo,GPIO.IN)        # Echo
GPIO.setup(redled,GPIO.OUT)     # Red LED
GPIO.setup(yellowled,GPIO.OUT)  # Yellow LED
GPIO.setup(greenled,GPIO.OUT)   # Green LED

# Set trigger and leds to False (Low)
GPIO.output(trigger, False)
GPIO.output(redled, False)
GPIO.output(yellowled, False)
GPIO.output(greenled, False)

# connect to miecraft instance
mc = minecraft.Minecraft.create()

# clear some working space
mc.postToChat("Welcome to Minecraft Pi! Clearing a play space.")
time.sleep(3)

mc.setBlocks(-50, -1, -50, 50, -1, 50, STONE)
mc.setBlocks(-50, 0, -50, 50, 50, 50, AIR)

mc.set.playerPos(0, 0, 0)

red = 0
yellow = 0
green = 0

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function.
try:

  while True:

    distance = measure_average()
    print ("Distance : %.1f" % distance)
    if distance < 10:
      GPIO.output(redled, True)
      mc.setBlock(0 + distance, red, 0, WOOL, RED)
      red=red+1
    elif distance < 30:
      GPIO.output(yellowled, True)
      mc.setBlock(0 + distance, yellow, 0 + distance, WOOL, YELLOW)
      yellow=yellow+1
    else:
      GPIO.output(greenled, True)
      mc.setBlock(0, green, 0 + distance/3, WOOL, GREEN)
      green=green+1
    time.sleep(1)
    # reset leds
    GPIO.output(redled, False)
    GPIO.output(yellowled, False)
    GPIO.output(greenled, False)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()
