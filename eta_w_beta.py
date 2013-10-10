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


towers = [0.07, 0.27, 0.44, 0.58, 0.72,0.83,0.93,1.04,1.14,1.24,1.36,1.48,1.61]
def toTower(x):
    for i in xrange(0,13):
        if (math.fabs(x) > towers[i]): continue;
        return i;


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


beta = [0.4, 0.5, 0.6, 0.7, 0.8,0.9,1.]
colors = ['b', 'g','r','c','m','y','k','w']

x=[[],[],[],[],[],[]];
z=[[],[],[],[],[],[]];
for i in xrange(0, len(rec)):
    for j in xrange(0,7):
        if (rec.Tbeta[i] > beta[j] or rec.Tbeta[i] <= 0.4):
            continue;
        x[j-1].append(toTower(rec.Teta[i]));
        if (rec.Tl1[i]):
            z[j-1].append(toTower(rec.Teta[i]))
        break;    



for i in xrange(0,6):
    histMC, bins =  np.histogram(x[i], bins=np.arange(0.,13.,1));
    histL1, bins = np.histogram(z[i], bins=np.arange(0.,13.,1));
    po = np.divide(np.array(histL1, dtype=float), np.array(histMC, dtype=float))
    #    plt.figure(i);
    plt.plot(np.arange(0.,12.,1), po, 'o', color=colors[i], label = str(beta[i])+r'<< $\beta$ <<'+str(beta[i+1]))


plt.xlabel(r'Tower')
plt.ylabel('Efficiency')
plt.title(r'Histogram of efficiency versus velocity')
plt.legend(loc=7)

#plt.subplots_adjust(left=0.15)

plt.draw()
plt.show()


del rec, x, z;
#arr = root2array(plik+'.root', 'Tbeta')
