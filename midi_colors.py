#!/usr/bin/env python3
import random
import os
import time
import subprocess
import mido
from huerc import *
from fade_between import *

pastels=[
{'hue':0, 'saturation':0}, # straight white
{'hue':10000, 'saturation':85}, # pale yellow
{'hue':45000, 'saturation':127}, # pale blue
]

max_hue=65535
max_brightness=255
max_saturation=255
bulbs=[4,1,2]
with mido.open_input() as inport:
    for msg in inport:
        if(msg.type == 'note_on' or msg.type == 'polytouch'):
          doSomething = False
          my_brightness = 127
          my_bulb = bulbs[int(msg.channel)]
          if (msg.type == 'note_on'):
            if (int(msg.velocity) == 0):
              killBulb(my_bulb)
            else:
              my_brightness = int(max_brightness * (int(msg.velocity)/127))
              doSomething = True
          else:
            if (int(msg.value) == 0):
              killBulb(my_bulb)
            else:
              my_brightness = int(max_brightness * (int(msg.value)/127))
              doSomething = True
          if doSomething:
            note=int(msg.note)
            if note < len(pastels):
              my_hue = pastels[note]['hue']
              my_saturation = pastels[note]['saturation']
            else:
              my_hue = int(max_hue * (note/(119-len(pastels))))
              my_saturation = 255
            startBulb(my_bulb)
            doColor(my_bulb, my_hue, my_brightness, my_saturation)
