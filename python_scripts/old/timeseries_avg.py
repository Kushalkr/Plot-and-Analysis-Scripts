#!/usr/bin/env python

# Script to average of the time series of the Vmax error from all directories 
# and create a single matrix.
# inputs are start hour, end hour and interval at which the perturbation 
# are introduced. tart hour is generally 540 and end hour is generally 4321 (all in mins), with interval 180 mins
# Author: Kushal


#def verr_avg(hstrt,hend,interval):
import numpy as np
import os
import sys

def readdata(exp_time_mins):
    exp_time = '{:05d}'.format(exp_time_mins)
    dir = "/Users/kkeshava/Downloads/Work/Model/HWRF/Excel_files/data/pert_amplitude_experiment/experiment1/"
    #   print("now in time t = " + str(time))
    #   os.system("cd " + dir+" ; ./vmax_tseries.sh exp_"+str(time).zfill(5))
    with open(dir+"time_series_exp_"+exp_time+".txt") as f:
        data = f.readlines()
    data_np = np.array([line.split()[1] for line in data]) 
    return data_np



def verr_calculate(hstrt,hend,pert_interval):
    """
   Returns verr and v_ref which is the error matrix and reference velocity.
  """
  
    i=1
    #vout = np.zeros((121,23),dtype=np.float64)
    verr = np.zeros((121,23),dtype=np.float64)
    v_ref = np.array(readdata(0)[:],dtype=np.float64)

    for time in range(hstrt,hend+1,pert_interval):
        vmean_np = np.zeros((121,))
        try:
            for j in range(-6,7,3):
                try:
                    print(i, (time + j))
                    #t = str(time + j).zfill(5)
                    # data_np = readdata(t)
                    data_np = np.array(readdata(t),dtype=np.float64)
                    vmean_np = vmean_np + data_np
                except:
                    continue
            vmean_np = vmean_np/5.
            #vout[:,i] = vmean_np
            verr[:,i] = vmean_np - v_ref
            i += 1
        except:
            continue
    #vout[:,0] = v_ref[:]
    verr = abs(verr)

    return verr, v_ref