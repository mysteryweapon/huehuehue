#!/usr/bin/python
import random
import os
import time
import subprocess
from huerc import *

bulbs=[3]
colors=[
        { 'hue': 8418, 'bri': 254, 'sat': 140},
        { 'hue': 1, 'bri': 60, 'sat': 255}
       ]

def doColor(bulb, hue, bri, sat):
    print("%s %s %s %s" %(bulb,hue,bri,sat))
    h=int(hue)
    b=int(bri)
    s=int(sat)
    os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
              '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
             % (hue_bridge, api_key, bulb, h, b, s))


def fadeBetween(colors, totaltime):
    interval=totaltime/100.0
    count=0
    for c in colors:
        for i in bulbs:
            doColor(i, c['hue'], c['bri'], c['sat'])
        if count < (len(colors) - 1):
            hdiff=abs(c['hue'] - colors[count+1]['hue'])
            bdiff=abs(c['bri'] - colors[count+1]['bri'])
            sdiff=abs(c['sat'] - colors[count+1]['sat'])
            hdiff/=100.0
            bdiff/=100.0
            sdiff/=100.0
            progress=0
            while progress < 100:
                if c['hue'] > colors[count+1]['hue']:
                    h = c['hue'] - int(hdiff*progress)
                else:
                    h = c['hue'] + int(hdiff*progress)
                if c['bri'] > colors[count+1]['bri']:
                    b = c['bri'] - int(bdiff*progress)
                else:
                    b = c['bri'] + int(bdiff*progress)
                if c['sat'] > colors[count+1]['sat']:
                    s = c['sat'] - int(sdiff*progress)
                else:
                    s = c['sat'] + int(sdiff*progress)
                for i in bulbs:
                    print("%s %s %s" % (hdiff, bdiff, sdiff))
                    print("%s" % progress)
                    doColor(i, h, b, s)
                progress+=1
                time.sleep(interval)
            count+=1


fadeBetween(colors,2700)
