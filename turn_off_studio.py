#!/usr/bin/python
import random
import os
import time
import subprocess
from huerc import *

max=255

for i in [4]:
    os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
              '{\"on\": false, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
             % (hue_bridge, api_key, i, 65535, max, 255))
