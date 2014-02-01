import sys 
import ROOT#gROOT, TCanvas, TF1, TFile
from root_numpy import root2array, root2rec, tree2rec
import os
import shutil
import math
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

rec = root2rec(plik+'.root', "T")
#np.where(rec.pt2<20, rec)


x = rec.diTauNSVfitMass;
#x = np.extract((rec.pt2 > 20)*(rec.pt1> 30)*(rec.pt1>200)*(rec.eta1>-20)*(rec.phi2>-20)*(rec.ptL1>20), rec.diTauNSVfitMass)

'''
x = np.arange(10)+2
print np.extract((x>3)*(x<7)*(x<5),x)

x = np.arange(10)+2
condlist = [x<3]
choicelist = [x]
#print np.select(condlist, choicelist)
x= np.extract(x<7, x)
print x
x=np.extract(x>3, x)

print x
#print y
'''
bin_width = 5;

histMC, bins =  np.histogram(x, bins=np.arange(0,500,bin_width));
#histL1, bins = np.histogram(y, bins=np.arange(-200,2000,bin_width));




#fig, ax1 = plt.subplots()

plt.bar(bins[:-1], histMC, width=bin_width, color='green', alpha=0.5, linewidth=None, label='MC')
#plt.bar(bins[:-1], histL1, width=bin_width, color='red', alpha=0.5, linewidth=None, label='L1')

plt.draw()
plt.show()

#del rec, x, z, po, ax1, ax2, bins, histMC, histL1;

'''
binned_values = np.digitize(column_of_values, bins_)
h= np.bincount(binned_values)
'''
