from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import random
import time
from scipy.misc import imread
from scipy.misc import imresize
import matplotlib.image as mpimg
import os
from scipy.ndimage import filters
import urllib

'''For scraping images.

Modified from Prof. Michael Guerzhoy:
http://www.cs.toronto.edu/~guerzhoy/321/proj1/get_data.py
'''

# act = list(set([a.split("\t")[0]
#                             for a in open("subset_actors.txt").readlines()]))
act = ['Gerard Butler', 'Daniel Radcliffe', 'Michael Vartan', 'Lorraine Bracco',
                                                'Peri Gilpin', 'Angie Harmon']

def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    '''From:
    http://code.activestate.com/recipes/473878-timeout-function-using-threading/'''
    import threading
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except:
                self.result = default

    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return False
    else:
        return it.result

testfile = urllib.URLopener()
# coords = open('coords.txt','w') # text file containing coordinates to crop by

# Note: you need to create the uncropped folder first in order for this to work

for a in act:
    last_name = a.split()[1].lower()
    i = 0
    for line in open("subset_actors.txt"):
        if a in line:
            split_line = line.split()
            id_= split_line[2]
            file_extension = split_line[4].split('.')[-1]
            filename = last_name + id_ + '.' + file_extension
            # A version without timeout (uncomment in case you need to
            # unsupress exceptions, which timeout() does)
            # testfile.retrieve(line.split()[4], "uncropped/"+filename)

            # timeout is used to stop downloading images taking too long
            timeout(testfile.retrieve, (split_line[4],
                                            "uncropped/" + filename), {}, 30)
            if os.path.isfile("uncropped/" + filename):
                # coords.write(filename + ' ' + line.split()[5] + '\n')
                print filename, split_line[5]

# coords.close()
