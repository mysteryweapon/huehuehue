#!/usr/bin/env python3
import random
import os
import time
import subprocess
from huerc import *
from fade_between import *

sleep_interval=.1
amount=1000
max=65535
bulbs=[4]

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
            doColor(i, mycolor, 255, 255)

            time.sleep(sleep_interval)
            count+=1

        c+=amount
