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

#z reki
#pliki=["ot001", "ot002", "ot009", "ot019", "ot020" , "nt001"]; 

#z konsoli
#pliki = [];
#for i in xrange(1, len(sys.argv)):
#     pliki += [str(sys.argv[i])]


plik=str(sys.argv[1]);

rec = root2rec(plik+'.root', "tvec")


towers = [0.07, 0.27, 0.44, 0.58, 0.72,0.83,0.93,1.04,1.14,1.24,1.36,1.48,1.61]
colors = ['b', 'g','r','c','m','y','k','w']
bin_width=0.01

x=[[],[],[],[],[],[],[],[],[],[],[],[],[]];
z=[[],[],[],[],[],[],[],[],[],[],[],[],[]];
for i in xrange(0, len(rec)):
    for j in xrange(0,13):
        if (math.fabs(rec.Teta[i]) > towers[j]):
            continue;
        x[j].append(rec.Tbeta[i]);
        if (rec.Tl1[i]):
            z[j].append(rec.Tbeta[i])
        break;    

for i in xrange(0,7):
    histMC, bins =  np.histogram(x[i], bins=np.arange(0.,1.01,bin_width));
    histL1, bins = np.histogram(z[i], bins=np.arange(0.,1.01,bin_width));
    po = np.divide(np.array(histL1, dtype=float), np.array(histMC, dtype=float))
    #    plt.figure(i);
    plt.plot(np.arange(0.01,1.01,bin_width), po, 'o-', color=colors[i], label = 'Wieza nr. '+str(i))

plt.xlim([0.3,1.01])
plt.ylim([0.,1.05])
plt.xlabel(r'$\beta$')
plt.ylabel('Efficiency')
plt.title(r'Histogram of efficiency versus velocity')
plt.legend(loc=2);

#plt.subplots_adjust(left=0.15)

plt.draw()
plt.show()

del rec, x, z;
