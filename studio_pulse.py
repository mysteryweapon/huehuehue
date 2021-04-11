#!/usr/bin/env python3
import random
import os
import time
import subprocess
from huerc import *

sleep_interval=.1
slices=60
max=255

for i in range(1,10):
    for i in [4]:
        b=max
        amount=int(max/slices)
        os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                  '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
                 % (hue_bridge, api_key, i, 65535, max, 255))


        while b > 0:
            os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                      '{\"bri\": %s}' -o - >/dev/null" \
                     % (hue_bridge, api_key, i, b))
            print("b: %s" % b);
            b-=amount
            time.sleep(sleep_interval)

        b=1
        while b < max:
            os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                      '{\"bri\": %s}' -o - >/dev/null" \
                     % (hue_bridge, api_key, i, b))
            print("b: %s" % b);
            b+=amount
            time.sleep(sleep_interval)
