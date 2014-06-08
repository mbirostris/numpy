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
from matplotlib import gridspec
from matplotlib.backends.backend_pdf import PdfPages


#plik=str(sys.argv[1]);
#plik2=str(sys.argv[2]);

try:
    os.mkdir("./rysunki/"+plik)
except:
    print "Jedziemyyyy...."

#"diTauVisMass","diTauNSVfitMass","visibleTauMass"
variable = 'diTauNSVfitMass'

#binowanie
#bins=[0., 20., 40., 60., 80., 100., 120., 140., 160., 180., 200., 250., 300., 350. ];
#bins=[0., 10.,  20., 30.,  40., 50.,  60., 70., 80.,90.,  100.,110., 120.,130., 140.,150., 160.,170., 180.,190., 200.,225., 250.,275., 300., 350. ];

bin_width = 6.0; bin_min = 0; bin_max = 360;
bins=np.arange(bin_min,bin_max,bin_width) 
bincount = (bin_max - bin_min)/bin_width;
#bin_width=[(bins[j+1]-bins[j]) for j in range(len(bins)-1)]
bin_width2=[(bins[j+1]-bins[j])/2 for j in range(len(bins)-1)]

#pliki
pliki=[ "TTbar", "WJets" ,"GGFH125", "VBFH125", "VH125", "DY->ll,j->t" ,"DY->ll, l->t", "Others" ,"LL" ,"DYtt"]; 
#QCD
pqcd = [];
for i in range(0, len(pliki)):
    if (pliki[i] == "GGFH125" or pliki[i]  == "VBFH125" or pliki[i]  == "VH125" or pliki[i] == "DY"):
        continue;
    pqcd.append("QCD_" + pliki[i]);

weighttableqcd=[19.712, 18.9235, 22.3695, 19.712, 19.712,19.712,19.712,19.712,19.712]

hqcd = []; hqcdw = [];
for i in xrange(0, len(pqcd)):
    hqcd.append(root2rec(pqcd[i]+'.root',variable)[variable]);
    hqcdw.append(root2rec(pqcd[i]+'_weight.root',variable)[variable]);

histqcd, bins = np.histogram(root2rec("QCD_Data"+'.root',variable)[variable], bins );
for i in range(0, len(hqcdw)):
    hist, bins  =  np.histogram(hqcd[i], bins, weights=hqcdw[i]);
    histqcd = histqcd - weighttableqcd[i]*hist;

histqcd = 1.06*histqcd;
X = np.array([bins[:-1],bins[1:]]).T.flatten()
Yqcd = np.array([histqcd,histqcd]).T.flatten()

# reszta MC
weighttable=[18.9235, 0.905*19.712, 19.712, 19.712, 19.712, 19.712, 19.712, 19.712, 19.712, 19.712];

h = [];hw = [];
for i in xrange(0, len(pliki)):
    h.append(root2rec(pliki[i]+'.root',variable)[variable]);
    hw.append(weighttable[i]*root2rec(pliki[i]+'_weight.root',variable)[variable]);

MChist = [];
for i in range(0,len(h)):
    hist, bins = np.histogram(h[i], bins, weights=hw[i]);
    MChist.append(hist);

histsum=histqcd; Ymc = [];
for i in range(0,len(MChist)):
    Ymc.append( np.array([MChist[i],MChist[i]]).T.flatten())
    histsum = histsum + MChist[i];


#rysowanie
fig = plt.figure(figsize=(16, 16)) 
gs = gridspec.GridSpec(16, 1) 
ax1 = plt.subplot(gs[0:12, :])

font = {'size'   : 28}
plt.rc('font', **font)


legenda=[r'$t\bar{t}$', "QCD" , 'EW', 'EW', 'EW', 'EW', r'$Z\to\mu\mu$', r'$Z\to\mu\mu$' , '', r'$Z\to\tau\tau$',  r'$Z\to\tau\tau$' ]
kolor=["#7575FF","#FF80FF",   "#7A0000",  "#7A0000", "#7A0000","#7A0000" ,"blue", "blue","black" ,"#FFD476", "#FFD476"]

plt.stackplot(X, Ymc[0], Yqcd, Ymc[1::1], colors=kolor, label='a') #plt.plot tez dzialaa

counts, bins = np.histogram(root2rec('Data'+'.root', variable)[variable], bins)
Ydata = np.array([counts,counts]).T.flatten()
dataERROR = np.sqrt(counts);
plt.plot(bins[:-1] + bin_width2 , counts, 'bo', markersize=16 ,color='black', label='Observed', linestyle='None')
#plt.errorbar( bins[:-1] + (bin_width+0.)/2, counts,yerr=dataERROR, fmt=None,color='black')

#legend
handles, labels = plt.gca().get_legend_handles_labels()
#print handles, labels
#plt.legend([handles[0], handles[9], handles[7], handles[3], handles[2], handles[1] ], [labels[0], labels[9], labels[7], labels[3], labels[2], labels[1]])
leg = plt.legend([handles[0],
    plt.Rectangle((0, 0), 1, 1, fc=kolor[9]), 
    plt.Rectangle((0, 0), 1, 1, fc=kolor[6]),
    plt.Rectangle((0, 0), 1, 1, fc=kolor[3]),
    plt.Rectangle((0, 0), 1, 1, fc=kolor[1]),
    plt.Rectangle((0, 0), 1, 1, fc=kolor[0])], 
    [labels[0],legenda[9], legenda[6], legenda[3], legenda[1], legenda[0]], numpoints=1, prop={'size':28})  #numpoints robi tylko jedna kropke w danych zamiast dwuch
leg.draw_frame(False)

#plt.grid(True,which="both",ls="-", color='red') #grid
plt.xlim([bin_min,bin_max])
ax1.set_xlabel(variable + ' (GeV)')
ax1.set_ylabel('Events/(' + str(bin_width) +' GeV)')

#data do MC
ax2  = plt.subplot(gs[14:, :])

po = np.divide(np.array(counts-histsum, dtype=float), np.array(histsum, dtype=float))
plt.plot(bins[:-1] + bin_width2, po, 'o', color='black', label='Efficiency', markersize=12)
plt.axhline(y=0, linestyle='-', color='red', linewidth=2, zorder=2)
ax2.set_ylabel(r'$\frac{{DATA - MC}}{MC}$')
plt.ylim([-3.5,3.5])
plt.xlim([bin_min,bin_max])

pp = PdfPages('multipage.pdf')
pp.savefig(fig)
pp.close()
#plt.draw()
#plt.show()
plt.close()


