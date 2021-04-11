#!/usr/bin/env python3
import random
import os
import time
from huerc import *

if hue_bridge == "" or api_key == "":
    print("You must configure your hue IP address or hostname and your api key in huerc.py first!!!")
    os._exit(255)

while True:
    color1=int(random.random()*65535)
    brightness1=int(random.random()*255)
    color2=int(random.random()*65535)
    brightness2=int(random.random()*255)
    color3=int(random.random()*65535)
    brightness3=int(random.random()*255)
    i="curl -XPUT http://%s/api/%s/lights/1/state -d '{\"hue\": %s, \"bri\": %s, \"sat\": %s}'" % (hue_bridge, api_key, color1, brightness1, int(random.random()*255))
    os.system(i)
    i="curl -XPUT http://%s/api/%s/lights/2/state -d '{\"hue\": %s, \"bri\": %s, \"sat\": %s}'" % (hue_bridge, api_key, color2, brightness2, int(random.random()*255))
    os.system(i)
    i="curl -XPUT http://%s/api/%s/lights/4/state -d '{\"hue\": %s, \"bri\": %s, \"sat\": %s}'" % (hue_bridge, api_key, color3, brightness3, int(random.random()*255))
    os.system(i)
