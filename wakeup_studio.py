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
fadeBetween(bulbs, colors,60)
