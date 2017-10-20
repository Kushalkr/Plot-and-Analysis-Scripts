#!/usr/bin/env python

# Script to create text file of time series
# once the queue job is complete.
#

import os

for time in range(0,4327,180):
    try:
      dir = "/N/u/kkeshava/scratch/hwrf-dtc-br2/experiment5/exp_"+str(time).zfill(5)
      print("now in time t = " + str(time))
      os.system("cd " + dir+" ; ./vmax_tseries.sh exp_"+str(time).zfill(5))
    except:
      continue
