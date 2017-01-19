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
    exp_time = str(exp_time_mins).zfill(5)
    dir = "/N/u/kkeshava/scratch/hwrf-dtc-br2/experiment1/exp_"+exp_time+"/"
    #   print("now in time t = " + str(time))
    #   os.system("cd " + dir+" ; ./vmax_tseries.sh exp_"+str(time).zfill(5))
    f=open(dir+"time_series_exp_"+exp_time+".txt")
    data_list = []
    for line in f:
        data_list.append(line.split())
    data_np = np.array(data_list)
    return data_np



def verr_calculate(hstrt,hend,pert_interval):
  """
   Returns verr and v_ref which is the error matrix and reference velocity.
  """
    i=1
    vout = np.zeros((121,23),dtype=np.float64)
    verr = np.zeros((121,23),dtype=np.float64)
    v_ref = np.array(readdata(0)[:,1],dtype=np.float64)

    for time in xrange(hstrt,hend,pert_interval):
        vmean_np = np.zeros((121,))
        try:
            for j in xrange(-6,7,3):
                try:
                    print i, (time + j)
                    #t = str(time + j).zfill(5)
                    data_np = readdata(t)
                    v_np = np.array(data_np[:,1],dtype=np.float64).T
                    vmean_np = vmean_np + v_np
                except:
                    continue
            vmean_np = vmean_np/5
            vout[:,i] = vmean_np
            verr[:,i] = vmean_np - v_ref
            i += 1
        except:
            continue
    vout[:,0] = v_ref[:]
    verr = abs(verr)

    return verr, v_ref
#saveas = '/N/u/kkeshava/scratch/hwrf-dtc-br2/experiment1/averaged_timeseries/verr_averaged.txt'
#np.savetxt(saveas,verr,fmt='%.3f',delimiter=' ,',newline='\n')
#return verr
