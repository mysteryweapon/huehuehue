#!/usr/bin/env python
import gtk.gdk
import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import colorsys
import os
import time
from huerc import *

NUM_CLUSTERS = 5
bulbs=[4]
sleep_interval=.01

while [ 1 ]:
  w = gtk.gdk.get_default_root_window()
  sz = w.get_size()
  print "The size of the window is %d x %d" % sz
  pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
  pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
  if (pb != None):
      pb.save("screenshot.png","png")
      print "Screenshot saved to screenshot.png."
  else:
      print "Unable to get the screenshot."

  print('reading image')
  im = Image.open('screenshot.png')
  im = im.resize((150, 150))      # optional, to reduce time
  ar = np.asarray(im)
  shape = ar.shape
  ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

  print('finding clusters')
  codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
  print('cluster centres:\n', codes)

  vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
  counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

  index_max = scipy.argmax(counts)                    # find most frequent
  peak = codes[index_max]
  colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
  print('most frequent is %s (#%s)' % (peak, colour))

  h,l,s = colorsys.rgb_to_hls(peak[0],peak[1],peak[2])
  print(int(h),int(l),int(s))

  for i in bulbs:
    os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
              '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
             % (hue_bridge, api_key, i, int(h), int(l), int(s)))
  time.sleep(sleep_interval)
