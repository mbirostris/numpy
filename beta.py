import ROOT#gROOT, TCanvas, TF1, TFile
from root_numpy import root2array, root2rec, tree2rec
import os
import shutil
import math
import sys
from ROOT import * #gROOT, TCanvas, TF1, TFile
import pylab as pl
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA


try:
    os.mkdir("./rysunki/tree/")
except:
    print "Jedziemyyyy...."

kolor=[1,2,9,2,3,2,8,9,7]

#z reki
#pliki=["ot001", "ot002", "ot009", "ot019", "ot020" , "nt001"]; 

#z konsoli
#pliki = [];
#for i in xrange(1, len(sys.argv)):
#     pliki += [str(sys.argv[i])]


plik=str(sys.argv[1]);

rec = root2rec(plik+'.root', "tvec")




x=[];z=[];
for i in xrange(0, len(rec)):
    if (math.fabs(rec.Teta[i]) < 1.61): 
        x.append(rec.Tbeta[i]);
        if (rec.Tl1[i]):
            z.append(rec.Tbeta[i])


histMC, bins =  np.histogram(x, bins=np.arange(0.,1.,0.01));
histL1, bins = np.histogram(z, bins=np.arange(0.,1.,0.01));


po = np.divide(np.array(histL1, dtype=float), np.array(histMC, dtype=float))



fig, ax1 = plt.subplots()
ax1.plot(np.arange(0.,0.99,0.01), po, 'r-', color='r')
ax1.set_xlabel('time (s)')
# Make the y-axis label and tick labels match the line color.
ax1.set_ylabel('Efficiency', color='r')

ax2 = ax1.twinx()
ax2.bar(bins[:-1], histMC, width=0.01, color='green', alpha=0.5)


ax3 = ax1.twinx()
ax3.bar(bins[:-1], histL1, width=0.01, color='blue', alpha=0.5)
ax3.set_ylabel('Events', color='g')



#plt.plot(np.arange(0.,0.99,0.01), po, 'go')
#plt.bar(bins[:-1], histMC, width=0.01, color='green', alpha=0.5)
#plt.bar(bins[:-1], histL1, width=0.01, color='blue', alpha=0.5)
#plt.xlim(min(bins), max(bins))


#plt.xlabel('Smarts')
#plt.ylabel('Probability')
#plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

#plt.subplots_adjust(left=0.15)

plt.draw()
plt.show()

'''
column_of_values = np.random.randint(10, 99, 10)

# set the bin values:
bins_ = np.array([0.0, 20.0, 50.0, 75.0])

binned_values = np.digitize(column_of_values, bins_)

print binned_values;

h= np.bincount(binned_values)

plt.plot()
plt.show();
'''

del rec, x, z;
#arr = root2array(plik+'.root', 'Tbeta')
