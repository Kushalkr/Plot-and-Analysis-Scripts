#!/usr/bin/env python

# Script to create text file of time series
# once the queue job is complete.
#

import os
#import numpy as np

shear = 0.0
while shear < 0.1:

#for shear in np.arange(0.0,0.46,0.05):
    try:
      dir = "/N/dc2/scratch/kkeshava/hwrf-dtc-br2/experiment_shear/12hr/exp_"+str(shear)
      print("now in shear = " + str(shear))
      print dir, type(dir)
      os.system("cd " + dir+" ; ./vmax_tseries.sh exp_"+str(shear))
      shear += 0.01
    except:
      shear += 0.01
      continue
