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


plik=str(sys.argv[1]);

try:
    os.mkdir("./rysunki/"+plik)
except:
    print "Jedziemyyyy...."

#z reki
#pliki=["ot001", "ot002", "ot009", "ot019", "ot020" , "nt001"]; 

#z konsoli
#pliki = [];
#for i in xrange(1, len(sys.argv)):
#     pliki += [str(sys.argv[i])]

rec = root2rec(plik+'.root', "tvec")


'''
x=[];z=[];
for i in xrange(0, len(rec)):
    if (math.fabs(rec.Teta[i]) < 1.61): 
        x.append(rec.Tbeta[i]);
        if (rec.Tl1[i]):
            z.append(rec.Tbeta[i])
'''

x = np.extract(np.absolute(rec.Teta) < 1.61, rec.Tbeta)
z = np.extract(rec.Tl1, rec.Tbeta)


bin_width = 0.01;

histMC, bins =  np.histogram(x, bins=np.arange(0.,1.01,bin_width));
histL1, bins = np.histogram(z, bins=np.arange(0.,1.01,bin_width));




po = np.divide(np.array(histL1, dtype=float), np.array(histMC, dtype=float))


fig, ax1 = plt.subplots()

leg1 = ax1.bar(bins[:-1], histMC, width=bin_width, color='green', alpha=0.5, linewidth=None, label='MC')
leg2 = ax1.bar(bins[:-1], histL1, width=bin_width, color='blue', alpha=0.5, linewidth=None, label='L1 Trigger') #bottom=histMC - robi stacka
ax1.set_ylabel('Events', color='g')
ax1.set_xlabel(r'$\beta$', color='black')
#ax1.set_ylim([0,max(histMC)]+0.1*max(histMC))
#ax1.set_xlim([0.,1.01])
#ax1.legend()

ax2 = ax1.twinx()
leg3  = ax2.plot(np.arange(0.01,1.01,bin_width), po, '^-', color='c', label='Efficiency')
ax2.set_ylabel('Efficiency', color='r')
plt.xlim([0.,1.01])

#plt.plot(np.arange(0.,0.99,0.01), po, 'go')
#plt.bar(bins[:-1], histMC, width=0.01, color='green', alpha=0.5)
#plt.bar(bins[:-1], histL1, width=0.01, color='blue', alpha=0.5)
#plt.xlim([0.,1.01])
#plt.ylabel('Probability')
#plt.xlabel('Probability')
plt.title(r'Histogram of efficiency versus velocity')
#plt.subplots_adjust(left=0.15)
#ax2.legend(loc=2)
#ax1.legend(loc=6)

plt.legend( (leg3[0], leg1, leg2), ('Efficiency', 'MC', 'L1 Trigger'), loc = 2 ) 

plt.draw()
plt.show()

del rec, x, z, po, ax1, ax2, bins, histMC, histL1;
'''
binned_values = np.digitize(column_of_values, bins_)
h= np.bincount(binned_values)
'''
