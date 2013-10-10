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

x = rec.Teta
z = np.extract(rec.Tl1, rec.Teta)

bin_width = 0.06;

histMC, bins =  np.histogram(x, bins=np.arange(-3.,3.06,bin_width));
histL1, bins = np.histogram(z, bins=np.arange(-3.,3.06,bin_width));


po = np.divide(np.array(histL1, dtype=float), np.array(histMC, dtype=float))

fig, ax1 = plt.subplots()

ax1.bar(bins[:-1], histMC, width=bin_width, color='green', alpha=0.5, linewidth=0)
ax1.set_ylabel('Events', color='g')
ax1.set_xlabel(r'$\eta$')
plt.ylim([0,max(histMC)]+0.1*max(histMC))


ax2 = ax1.twinx()
ax2.bar(bins[:-1], histL1, width=bin_width, color='blue', alpha=0.5, linewidth=0)
plt.ylim([0,max(histMC)]+0.1*max(histMC))

ax3 = ax2.twinx()
ax3.plot(np.arange(-2.99,3.06,bin_width), po, 'o-', color='r')
ax3.set_ylabel('Efficiency', color='r')

#plt.xlabel('Smarts')
#plt.ylabel('Probability')
plt.title(r'Histogram of efficiency versus pseudorapidity')

#plt.subplots_adjust(left=0.15)

plt.draw()
plt.show()

del rec, x, z;
