#!/usr/bin/python
import random
import os
import time
import subprocess
from huerc import *
from fade_between import *
bulbs=[3]
colors=[
        { 'hue': 8418, 'bri': 254, 'sat': 140},
        { 'hue': 1, 'bri': 80, 'sat': 255}
       ]


while True:
    for i in bulbs:
        color = int(subprocess.check_output("curl -s -XGET http://%s/api/%s/lights/%s|jq .state.hue" \
                                               % (hue_bridge, api_key, i), shell=True))
    print(color)
    if color == 8418:
        fadeBetween(bulbs, colors,60)

    time.sleep(60)
done

