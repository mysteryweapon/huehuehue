#!/usr/bin/env python3
import random
import os
import time
import subprocess
from huerc import *

fractional_constant=.04
ms_sleep=.3
if hue_bridge == "" or api_key == "":
    print("You must configure your hue IP address or hostname and your api key in huerc.py first!!!")
    os._exit(255)

def newscheme():
    cseed = int(random.random()*65535)
    bseed = int(random.random()*255)
    sseed = int(random.random()*255)
    count = 0
    for i in target_colors:
        c_jitter = int(random.random()*6000)
        b_jitter = int(random.random()*15)
        s_jitter = int(random.random()*15)
        if int(random.random()*2) > 0:
            c_val = cseed - c_jitter
        else:
            c_val = cseed + c_jitter

        if int(random.random()*2) > 0:
            b_val = bseed - b_jitter
        else:
            b_val = bseed + b_jitter


        if int(random.random()*2) > 0:
            s_val = sseed - s_jitter
        else:
            s_val = sseed + s_jitter

        if (b_val > 255):
            b_val=255
        if (b_val < 1):
            b_val=1
        if (s_val > 255):
            s_val=255
        if (s_val < 1):
            s_val=1
        if (c_val > 65535):
            c_val=65535
        if (c_val < 1):
            c_val=1

        target_colors[count] =  {"bulb": i["bulb"], "color": c_val, "brightness": b_val, "saturation": s_val, "cslice": 0, "bslice": 0, "sslice": 0}

        count = count + 1

def newdone():
    for i in target_colors:
        print("added")
        done.append(False)


target_colors = [
                    {"bulb": 4}
                ]

newscheme()
done=[]
current_colors = []
newdone()
#print("coiunt %s" % str(done))
#time.sleep(2)
for i in target_colors:
        print("bulb %s" % i["bulb"])
        color = int(subprocess.check_output("curl -s -XGET http://%s/api/%s/lights/%s|jq .state.hue" \
                                               % (hue_bridge, api_key, i["bulb"]), shell=True))

        brightness = int(subprocess.check_output("curl -s -XGET http://%s/api/%s/lights/%s|jq .state.bri" \
                                               % (hue_bridge, api_key, i["bulb"]), shell=True))

        saturation = int(subprocess.check_output("curl -s -XGET http://%s/api/%s/lights/%s|jq .state.sat" \
                                               % (hue_bridge, api_key, i["bulb"]), shell=True))

        current_colors.append({"color": color, "brightness": brightness, "saturation": saturation})


while True:
    count=0
    dark=False
    nova=False
    if int(random.random()*20000000) > 19500000:
        dark=True
    elif int(random.random()*20000000) > 19500000:
        nova=True
    for i in target_colors:
        color = current_colors[count]["color"]
        brightness = current_colors[count]["brightness"]
        saturation = current_colors[count]["saturation"]
        print("current color: %s" % color)
        print("current brightness: %s" % brightness)
        print("current saturation: %s" % saturation)
        print("bulb: %s c: %s b: %s s: %s bslice: %s cslice: %s sslice: %s" % (i["bulb"], i["color"], i["brightness"], i["saturation"], i["bslice"], i["cslice"], i["sslice"]))
        if i["cslice"] == 0 and i["bslice"] == 0 and i["sslice"] == 0:
            c = int(abs(int(color) - i["color"]) * fractional_constant)
            b = int(abs(int(brightness) - i["brightness"]) * fractional_constant)
            s = int(abs(int(saturation) - i["saturation"]) * fractional_constant)
            if c < 1:
                c = 1
            if b < 1:
                b = 1
            if s < 1:
                s = 1
            target_colors[count] = {"bulb": i["bulb"], "color": i["color"], "brightness": i["brightness"], "saturation": i["saturation"], "cslice": c, "bslice": b, "sslice": s}
        if color == i["color"] and brightness == i["brightness"] and saturation == i["saturation"]:
            alldone = True
            done[count] = True
            for i in done:
                if i == False:
                    alldone = False

            if alldone == True:
                done=[]
                newdone()
                newscheme()
        else:
          newB=0
          newC=0
          newS=0
          if abs(brightness - i["brightness"]) <= i["bslice"]:
            newB=i["brightness"]
          elif brightness > i["brightness"]:
            newB = brightness - i["bslice"]
          elif brightness < i["brightness"]:
            newB = brightness + i["bslice"]

          if abs(saturation - i["saturation"]) <= i["sslice"]:
            newS=i["saturation"]
          elif saturation > i["saturation"]:
            newS = saturation - i["sslice"]
          elif saturation < i["saturation"]:
            newS = saturation + i["sslice"]

          if abs(color - i["color"]) <= i["cslice"]:
            newC=i["color"]
          elif color > i["color"]:
            newC = color - i["cslice"]
          elif color < i["color"]:
            newC = color + i["cslice"]

          if dark:
            os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d '{\"on\": false}' -o - >/dev/null" \
                     % (hue_bridge, api_key, i["bulb"]))

          elif nova:
            os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                      '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
                     % (hue_bridge, api_key, i["bulb"], \
                        int(random.random()*65535), 255, 255))

          elif int(random.random()*20000000) > 19500000:
            os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d '{\"on\": false}' -o - >/dev/null" \
                     % (hue_bridge, api_key, i["bulb"]))

          elif int(random.random()*20000000) > 19500000:
            os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                      '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
                     % (hue_bridge, api_key, i["bulb"], \
                        int(random.random()*65535), int(random.random()*255), int(random.random()*255)))
          else:
            os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
                      '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
                     % (hue_bridge, api_key, i["bulb"], \
                        newC, newB, newS))

          # update internal tracker
          current_colors[count] = {"color": newC, "brightness": newB, "saturation": newS}

        count = count + 1

    time.sleep(ms_sleep)
