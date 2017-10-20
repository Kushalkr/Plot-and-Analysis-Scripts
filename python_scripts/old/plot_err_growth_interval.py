#!/usr/bin/env python

# Script to plot the time series of the Error growth in Vmax
# 36 hours from the time of perturbation
# Author: Kushal

import numpy as np
import matplotlib.pyplot as plt
#import seaborn
import sys

exp_num = 4
interval=18

fig, ax = plt.subplots(figsize=(16,9))
plt.hold(True)
cmap = plt.cm.rainbow
clist = [0.1, 0.3, 0.5,0.8,0.9]
for i in np.linspace(0.8,0.95,16):
  clist.append(i)
clist = np.array(clist)
colors = [cmap(i) for i in clist]
ax.set_color_cycle(colors)
for time in range(0,4321,180):
  try:
    t = str(time).zfill(5)
    hstrt = time / 60
    hend = hstrt + interval
    dir = "/N/u/kkeshava/scratch/hwrf-dtc-br2/experiment"+str(exp_num)+"/exp_"+t+"/"
#	print("now in time t = " + str(time))
#	os.system("cd " + dir+" ; ./vmax_tseries.sh exp_"+str(time).zfill(5))

    f=open(dir+"time_series_exp_"+t+".txt")
    data = []
    for line in f:
        data.append(line.split())
    f.close()
    data = np.array(data)
    times = np.array(data[:,0],dtype=np.int64)
    if time == 0:
      vmax_0 = np.array(data[:,1], dtype=np.float64)
      continue
    vmax = np.array(data[:,1], dtype=np.float64)
    verr = np.array(data[:,1], dtype=np.float64)
    verr[:] = 'nan'
    for k in range(hstrt,hend):
        verr[k] = abs(vmax[k] - vmax_0[k])
    print verr
    ax.plot(times,verr,'-',label=str(hstrt)+'hr')#, linewidth=1.0)
#leg.get_frame().set_color('white')
  except:
    continue
ax.set_xlabel('Time in hours', fontweight='bold', fontsize=14)
xt = range(0,121,12)
#yt = [0.0, 0.5, 1.0, 1.5, 2.0]
yt = [0.0, 0.5, 1.0, 1.5, 2.0,2.5,3.0,3.5,4.0,4.5,5.0]
ax.set_xticks(xt)
ax.set_xticklabels(xt,fontsize=12, fontweight='demibold')
ax.set_yticks(yt)
ax.set_yticklabels(yt,fontsize=12, fontweight='demibold')
ax.set_ylabel(r'V$_{max}$ Error', fontweight='bold', fontsize=14)
ax.set_title(r'Error Growth of V$_{max}$ with Perturbation of 1 $ms^{-1}$ (Only Domain 1)', fontweight='bold', fontsize=18)
leg = ax.legend(loc='upper left', prop={'size':11, 'weight':'demibold'}, frameon=True,framealpha=1.0)


ax2 = ax.twinx()
ax2.plot(times,vmax_0,'k', linewidth=2)
ax2.set_ylabel('Vmax (unperturbed)')
plt.savefig('/N/u/kkeshava/Karst/plots/Err_Vmax_no_ensemble_timeseries_expt'+str(exp_num)+'.pdf',dpi=200)
#plt.show()
