#!/usr/bin/env python

# Script to create text file of time series
# once the queue job is complete.
#

import os

for sst in range(297,306,1):
  for time in range(0,4327,180):
    try:
      dir = "/N/u/kkeshava/scratch/hwrf-dtc-br2/experiment_sst/"+str(sst)+"/exp_"+str(time).zfill(5)
      print(dir)
      os.system("cd " + dir+" ; ./vmax_tseries.sh exp_"+str(time).zfill(5))
    except:
      continue
