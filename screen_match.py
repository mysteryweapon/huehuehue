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
sleep_interval=1
def pixbuf2image(pix):
    """Convert gdkpixbuf to PIL image"""
    data = pix.get_pixels()
    w = pix.props.width
    h = pix.props.height
    stride = pix.props.rowstride
    mode = "RGB"
    if pix.props.has_alpha == True:
        mode = "RGBA"
    im = Image.frombytes(mode, (w, h), data, "raw", mode, stride)
    return im

while [ 1 ]:
  w = gtk.gdk.get_default_root_window()
  sz = w.get_size()
  print "The size of the window is %d x %d" % sz
  pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
  pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
  im = pixbuf2image(pb)
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

  #r=int(peak[0]/255)
  #g=int(peak[1]/255)
  #b=int(peak[2]/255)
  r=peak[0]/255
  g=peak[1]/255
  b=peak[2]/255
  print(r,g,b)
  h,s,l=colorsys.rgb_to_hsv(r,g,b)
  h *= 255
  h *= 255
  s *= 255
  l *= 255
  print(h,s,l)

  for i in bulbs:
    #print("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
    #          '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
    #         % (hue_bridge, api_key, i, int(h), int(l), int(s)))
    os.system("curl -XPUT -s http://%s/api/%s/lights/%s/state -d \
              '{\"on\": true, \"hue\": %s, \"bri\": %s, \"sat\": %s}' -o - >/dev/null" \
             % (hue_bridge, api_key, i, int(h), int(l), int(s)))
  time.sleep(sleep_interval)
