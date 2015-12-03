#!/usr/bin/env python

import RPi.GPIO as gpio
import os
import time

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
lights = 0

while True:
    b1 = gpio.input(4)
    b2 = gpio.input(17)
    if (b1 == False):
       if lights == 0:
           os.system("export SYNCHRONIZED_LIGHTS_HOME=/home/pi/lightshowpi; sudo python /home/pi/lightshowpi/py/hardware_controller.py --state=on")
           lights = 1
       elif lights == 1:
           os.system("export SYNCHRONIZED_LIGHTS_HOME=/home/pi/lightshowpi; sudo python /home/pi/lightshowpi/py/hardware_controller.py --state=off")
           lights = 0
    if (b2 == False):
       if lights == 0:
           os.system("export SYNCHRONIZED_LIGHTS_HOME=/home/pi/lightshowpi; sudo lightshowpi/bin/start_music_and_lights")
           lights = 1
       elif lights == 1:
           os.system("export SYNCHRONIZED_LIGHTS_HOME=/home/pi/lightshowpi; sudo lightshowpi/bin/stop_music_and_lights")
           lights = 0
    time.sleep(0.2)
