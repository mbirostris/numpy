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


PtBins=[0., 0.1,1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5., 6., 7., 8.,10., 12., 14., 16., 18., 20., 25., 30., 35., 40., 45.,50., 60., 70., 80., 90., 100., 120., 140.,160.];
 
PtWidth=[(PtBins[j+1]-PtBins[j]) for j in range(len(PtBins)-1)]  

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

x = np.extract(np.absolute(rec.Teta) < 1.61, rec.Tpt)
z = np.extract(rec.Tl1, rec.Tpt)

bin_width = 2;

histMC, bins =  np.histogram(x, bins=PtBins);
histL1, bins = np.histogram(z, bins=PtBins);

po = np.divide(np.array(histL1, dtype=float), np.array(histMC, dtype=float))

fig, ax1 = plt.subplots()

ax1.bar(bins[:-1], histMC, width=PtWidth , color='green', alpha=0.5, linewidth=None, label='llllaaa')
ax1.bar(bins[:-1], histL1, width=PtWidth, color='blue', alpha=0.5, linewidth=None, label='ss')
ax1.set_ylabel('Events', color='g')
ax1.set_xlabel(r'$\beta$', color='black')
plt.ylim([0,max(histMC)]+0.1*max(histMC))
plt.xlim([0,max(PtBins)])
ax1.set_xscale('log')
#ax1.legend()

ax2 = ax1.twinx()
ax2.plot(PtBins[1:], po, 'o-', color='r', label='Efficiency')
ax2.set_ylabel('Efficiency', color='r')
plt.xlim([0,max(PtBins)])
ax2.set_xscale('log')

#plt.plot(np.arange(0.,0.99,0.01), po, 'go')
#plt.bar(bins[:-1], histMC, width=0.01, color='green', alpha=0.5)
#plt.bar(bins[:-1], histL1, width=0.01, color='blue', alpha=0.5)
#plt.xlim(min(PtBins), max(PtBins)+2)
#plt.ylabel('Probability')
#plt.xlabel('Probability')
plt.title(r'Histogram of efficiency versus velocity')
#plt.subplots_adjust(left=0.15)

plt.draw()
plt.show()

del rec, x, z, po, ax1, ax2, ax3, bins, histMC, histL1;
'''
binned_values = np.digitize(column_of_values, bins_)
h= np.bincount(binned_values)
'''
