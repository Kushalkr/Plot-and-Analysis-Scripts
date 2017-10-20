import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pygrib

cycle = '2016093000'
stormname = 'matthew'
stormid = '14L'
hwrfcom = '/N/dc2/scratch/kkeshava/hwrfv3.8a/hwrfrun/output/pytmp/hwrfrun/com/' 

u10m = []

for itime in range(0,127,3):
    print 'In fcst '+ str(itime).zfill(3) + ' hrs'
    grbs = pygrib.open(hwrfcom + cycle + '/' + stormid + '/' + \
            stormname + stormid.lower() + '.' + cycle + '.' + \
            'hwrfprs.core.0p02.f' + str(itime).zfill(3) + '.grb2')

    for grb in grbs:
        if grb.shortName == '10u':
            u10m.append(grb.values)
    grbs.close()

u10m = np.array(u10m)


