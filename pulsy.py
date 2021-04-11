#!/usr/bin/env python3
import random
import os
import time
import subprocess
from huerc import *

sleep_interval=.1
amount=2
max=60

while True:
    for i in [3]:
        b=60
        os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                  '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
                 % (hue_bridge, api_key, i, 65535, max, 255))


        while b > 0:
            os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                      '{\"bri\": %s}' -o - >/dev/null" \
                     % (hue_bridge, api_key, i, b))
            b-=amount
            time.sleep(sleep_interval)

        b=amount
        while b < max:
            os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                      '{\"bri\": %s}' -o - >/dev/null" \
                     % (hue_bridge, api_key, i, b))
            b+=amount
            time.sleep(sleep_interval)
