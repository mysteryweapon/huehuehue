#!/usr/bin/env python3
import random
import os
import time
import subprocess
from huerc import *
from fade_between import *
bulbs=[4]
colors=[
        { 'hue': 1, 'bri': 1, 'sat': 255},
        { 'hue': 40552, 'bri': 254, 'sat': 8}
       ]


while True:
    for i in bulbs:
        color = int(subprocess.check_output("curl -s -XGET http://%s/api/%s/lights/%s|jq .state.hue" \
                                               % (hue_bridge, api_key, i), shell=True))
        sat = int(subprocess.check_output("curl -s -XGET http://%s/api/%s/lights/%s|jq .state.sat" \
                                               % (hue_bridge, api_key, i), shell=True))
        bri = int(subprocess.check_output("curl -s -XGET http://%s/api/%s/lights/%s|jq .state.bri" \
                                               % (hue_bridge, api_key, i), shell=True))
    print(color)
    print(sat)
    print(bri)
#    if color != colors[1]["hue"]:
#        fadeBetween(bulbs, colors,60)

    time.sleep(60)
done

