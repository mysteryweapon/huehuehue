#!/usr/bin/python
import random
import os
import time
import subprocess
from huerc import *

sleep_interval=.1
amount=1000
max=65535
bulbs=[1,2,4]

while True:
    c = amount
    while c < max:
        count=0
        for i in bulbs:
            mycolor=0
            mycolor+=(max/len(bulbs) * (count))
            mycolor+=c
            while mycolor > max:
                mycolor-=max

            os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                      '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
                     % (hue_bridge, api_key, i, mycolor, 255, 255))

            time.sleep(sleep_interval)
            count+=1

        c+=amount
