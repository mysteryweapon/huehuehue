#!/usr/bin/python
import random
import os
import time
import subprocess
from huerc import *

sleep_interval=0.3
sleep_interval2=1
bulbs=[1,2,4]
a=0
max=18

while a < 18:
    for i in bulbs:
        os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                  '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
                 % (hue_bridge, api_key, i, int(random.random()*65535), 255, 255))

        time.sleep(sleep_interval2)

        os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d '{\"on\": false}' -o - >/dev/null" \
                 % (hue_bridge, api_key, i))

        time.sleep(sleep_interval)
        a+=1

for i in bulbs:
        os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                  '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
                 % (hue_bridge, api_key, i, int(random.random()*65535), 255, 1))
