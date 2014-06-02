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
from matplotlib.backends.backend_pdf import PdfPages


pp = PdfPages('multipage.pdf')
plik=str(sys.argv[1]);

try:
    os.mkdir("./rysunki/")
except:
    print "Jedziemyyyy...."

#z reki
#pliki=["ot001", "ot002", "ot009", "ot019", "ot020" , "nt001"]; 

#z konsoli
#pliki = [];
#for i in xrange(1, len(sys.argv)):
#     pliki += [str(sys.argv[i])]
aaa = plt.figure(1)
a = 0; b = 0; c = 0;
for i in xrange(1,len(sys.argv)):
#    plt.figure(i)
    rec = root2rec(sys.argv[i], "tvec")
       
    #x = np.extract(np.absolute(rec.Teta) < 1.61, rec.Tbeta)
    x0 =  rec.Tlbx0; x_1 =  rec.Tlbx_1; x1 =  rec.Tlbx1; pt = rec.TptT0;
    for i in xrange(0, len(x0)):
        if (pt[i] > 16): a += int(x0[i])
    for i in xrange(0, len(x_1)):
        if (pt[i] > 16): b += int(x_1[i])
    for i in xrange(0, len(x1)):
        if (pt[i] > 16): c += int(x1[i])
    
    rect = plt.bar([-1.5,-0.5,0.5], [float(b)/a,float(a)/a,float(c)/a],  linewidth=2,width=1, label="line 1")
    plt.draw()
    print b, a, c
    #pl.stem([-1,0,1], [b,a,c],  linefmt='b-.', markerfmt='bo', basefmt='r-' )
    #pl.setp(markerline, 'markerfacecolor', 'b')
    #pl.setp(baseline, 'color','r','linewidth',  3)
    #plt.ylim([-10,1000000])
#plt.legend(loc='upper right', shadow=True)
plt.xlim([-2,2])
plt.yscale('log')
plt.ylim([0.00001,2])
plt.xlabel('BX')
plt.ylabel('Liczba przypadkow')
pp.savefig(aaa)
plt.show()

PtBins=[0., 0.1,1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5., 6., 7., 8.,10., 12., 14., 16., 18., 20., 25., 30., 35., 40., 45.,50., 60., 70., 80., 90., 100., 120., 140.,160.];

PtWidth=[(PtBins[j+1]-PtBins[j]) for j in range(len(PtBins)-1)]

'''
for i in xrange(1,len(sys.argv)):
    aaa=plt.figure(i+1)
    rec = root2rec(sys.argv[i], "tvec")
       
    #x = np.extract(np.absolute(rec.Teta) < 1.61, rec.Tbeta)
    x =  np.extract(np.logical_and(np.absolute(rec.Teta0) < 1.61, rec.Tpt0 > 10 ), rec.Tpt0); y = np.extract(np.logical_and(np.logical_and(np.absolute(rec.Teta0) < 1.61, rec.Tlbx0), rec.Tpt0 > 10), rec.Tpt0);
    histMC, bins =  np.histogram(x, bins=PtBins);
#    print bins;
    histL1, bins = np.histogram(y, bins=PtBins);
    po = np.divide(np.array(histL1, dtype=float), np.array(histMC, dtype=float))
    plt.plot(PtBins[1:], po, 'o-', color='r', label='Efficiency')
#    plt.xscale('log')
    plt.ylabel('Efektywnosc')
    plt.xlabel('Ped poprzeczny')
    plt.draw()
    pp.savefig(aaa)
#    plt.show()

pp.close()
#y=np.array([b,a,c])
'''
'''
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
'''
binned_values = np.digitize(column_of_values, bins_)
h= np.bincount(binned_values)
'''
