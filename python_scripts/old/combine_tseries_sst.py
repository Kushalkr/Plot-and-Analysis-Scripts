#!/usr/bin/env python

# Script to combine velocities from the time series into a single file
# 
#
import sys
import os

try:
  dir = "/N/u/kkeshava/scratch/hwrf-dtc-br2/experiment_sst/"+str(sst)
  os.system("cd " + dir+" ; paste exp_0*/time_series*.txt | awk '{print $}' exp_"+str(range(540,4321,180)).zfill(5)+"/time_series*.txt )")
except:
  print "Something wrong"
  sys.exit()
