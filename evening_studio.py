#!/usr/bin/python
import random
import os
import time
import subprocess
from huerc import *
from fade_between import *
bulbs=[4]
colors=[
        { 'hue': 40552, 'bri': 255, 'sat': 8},
        { 'hue': 65068, 'bri': 255, 'sat': 255}
       ]
fadeBetween(bulbs, colors,60)
