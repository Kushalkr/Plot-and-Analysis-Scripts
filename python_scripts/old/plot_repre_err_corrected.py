#!/usr/bin/env python

# Script to plot the time series of the Error growth in Vmax
# 'interval' hours from the time of perturbation
# Author: Kushal

import numpy as np
import matplotlib.pyplot as plt
#import seaborn
import sys
from timeseries_avg import verr_calculate

exp_num = 1
interval=18

hstrt = 540
hend = 4321
pert_interval = 180

verr, vref = verr_calculate(hstrt, hend, pert_interval)
times = range(121)

fig, ax = plt.subplots(figsize=(16,9))
plt.hold(True)
cmap = plt.cm.rainbow
clist = [0.1, 0.3, 0.5,0.8,0.9]
for i in np.linspace(0.8,0.95,16):
  clist.append(i)
clist = np.array(clist)
colors = [cmap(i) for i in clist]
ax.set_color_cycle(colors)

i = 1
for time in range(540,4321,180):
    hstrt = time/60
    hend = hstrt + interval
    t = str(time).zfill(5)
    verr[hend:,i] = 'nan'
#    for k in range(hstrt,hend):
#        verr[:] = abs(vmax[k] - vmax_0[k])
#    print verr
    ax.plot(times,verr[:,i],'-',label=str(hstrt)+'hr')#, linewidth=1.0)
    i = i + 1
ax.set_xlabel('Time in hours', fontweight='bold', fontsize=14)
xt = range(0,121,12)
yt = [0.0, 0.5, 1.0, 1.5, 2.0]
ax.set_xticks(xt)
ax.set_xticklabels(xt,fontsize=12, fontweight='demibold')
ax.set_yticks(yt)
ax.set_yticklabels(yt,fontsize=12, fontweight='demibold')
ax.set_ylabel(r'V$_{max}$ Error', fontweight='bold', fontsize=14)
ax.set_title(r'Error Growth of V$_{max}$ with Perturbation of 1 $ms^{-1}$', fontweight='bold', fontsize=18)
leg = ax.legend(loc='upper left', prop={'size':11, 'weight':'demibold'}, frameon=True,framealpha=1.0)


ax2 = ax.twinx()
ax2.plot(times,vref,'k', linewidth=2)
ax2.set_ylabel('Vmax (unperturbed)')
plt.savefig('/N/u/kkeshava/Karst/plots/Err_Vmax_with_ensemble_expt'+str(exp_num)+'.pdf',dpi=200)
plt.show()
