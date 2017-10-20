#!/usr/bin/env python
# Script to plot the time series of the Error in Vmax
# Author: Kushal

import numpy as np
import matplotlib.pyplot as plt
#import seaborn


fig, ax = plt.subplots(figsize=(16,9))
plt.hold(True)


for time in range(0,4321,180):
  try:
    t = str(time).zfill(5)
    t2 = time / 60.
    dir = "/N/u/kkeshava/scratch/hwrf-dtc-br2/experiment1/exp_"+t+"/"
#	print("now in time t = " + str(time))
#	os.system("cd " + dir+" ; ./vmax_tseries.sh exp_"+str(time).zfill(5))

    f=open(dir+"time_series_exp_"+t+".txt")
    data = []
    for line in f:
        data.append(line.split())
    data = np.array(data)
    times = np.array(data[:,0],dtype=np.int64)
    vmax = np.array(data[:,1],dtype=np.float64)
    if time == 0:
      vmax_0 = vmax.copy()
      continue
    verr = vmax - vmax_0
    ax.plot(times,abs(verr),'-',label=str((time/60))+'hr', linewidth=1.0)
#leg.get_frame().set_color('white')
  except:
    continue
ax.set_xlabel('Time in hours', fontweight='bold', fontsize=14)
xt = range(0,121,12)
yt = range(0,8,1)
ax.set_xticks(xt)
ax.set_xticklabels(xt,fontsize=12, fontweight='demibold')
ax.set_yticks(yt)
ax.set_yticklabels(yt,fontsize=12, fontweight='demibold')
ax.set_ylabel(r'V$_{max}$', fontweight='bold', fontsize=14)
ax.set_title(r'Error Growth of V$_{max}$ with Perturbation of 1 $ms^{-1}$', fontweight='bold', fontsize=18)
leg = ax.legend(loc='best', prop={'size':'large', 'weight':'demibold'}, frameon=True,framealpha=1.0)
plt.savefig('/N/u/kkeshava/Karst/plots/Err_Vmax_full_timeseries_expt1.pdf',dpi=200)
plt.show()
