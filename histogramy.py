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

#plik=str(sys.argv[1]);
#plik2=str(sys.argv[2]);

try:
    os.mkdir("./rysunki/"+plik)
except:
    print "Jedziemyyyy...."


data="data";# dataw="backgroundTTbar_weight"
recdata=  root2rec(data+'.root', "T")
hdata = recdata.diTauNSVfitMass;

pliki=[ "backgroundTTbar", "backgroundWJets" , "GGFH125", "VBFH125", "VH125", "backgroundDYJtoTau" , "backgroundDYMutoTau", "backgroundOthers" ,"backgroundDYTauTauLL" ,"backgroundDYTauTau"  ]; 

plikiw=["backgroundTTbar_weight", "backgroundWJets_weight" , "GGFH125_weight", "VBFH125_weight", "VH125_weight", "backgroundDYJtoTau_weight", "backgroundDYMutoTau_weight", "backgroundOthers_weight" , "backgroundDYTauTauLL_weight" ,"backgroundDYTauTau_weight"];

weighttable=[18.9235, 0.905*19.712, 19.712, 19.712, 19.712, 19.712, 19.712, 19.712, 19.712, 19.712];
#weighttable=[18.9235, 22.3695, 0, 0, 0, 19.712, 19.712, 19.712, 19.712, 19.712];

legenda=[r'$t\bar{t}$', 'EW', 'EW', 'EW', 'EW', r'$Z\to\mu\mu$', r'$Z\to\mu\mu$' , '', r'$Z\to\tau\tau$',  r'$Z\to\tau\tau$' ]

kolor=[ "#7575FF", "#7A0000",  "#7A0000", "#7A0000","#7A0000" ,"blue", "blue","black" ,"#FFB84D", "#FFB84D" ,"red"]

h = [];hw = [];
for i in xrange(0, len(pliki)):
    h.append(root2rec(pliki[i]+'.root',"T").diTauNSVfitMass);
    hw.append(root2rec(plikiw[i]+'.root',"T").diTauNSVfitMass);
 

for i in range(0, len(hw)):
    hw[i] = hw[i]*weighttable[i];


#bins=[0., 20., 40., 60., 80., 100., 120., 140., 160., 180., 200., 250., 300., 350. ];
#bins=[0., 10.,  20., 30.,  40., 50.,  60., 70., 80.,90.,  100.,110., 120.,130., 140.,150., 160.,170., 180.,190., 200.,225., 250.,275., 300., 350. ];

bin_width = 6;
bins=np.arange(0,400,bin_width) 

bin_width=[(bins[j+1]-bins[j]) for j in range(len(bins)-1)]
bin_width2=[(bins[j+1]-bins[j])/2 for j in range(len(bins)-1)]

fig = plt.figure(figsize=(8, 6)) 
gs = gridspec.GridSpec(8, 1) 

ax1 = plt.subplot(gs[0:6, :])

#QCD
pqcd=["QCDJtoTau","QCDttbar","QCDwjets", "QCDOthers"]
pqcdw=["QCDJtoTau_weight","QCDttbar_weight","QCDwjets_weight", "QCDOthers_weight"]
weighttableqcd=[19.712, 18.9235, 22.3695, 19.712, 19.712]

hqcd = []; hqcdw = [];
for i in xrange(0, len(pqcd)):
    hqcd.append(root2rec(pqcd[i]+'.root',"T").diTauNSVfitMass);
    hqcdw.append(root2rec(pqcdw[i]+'.root',"T").diTauNSVfitMass);
 

histqcd, bins =  np.histogram(root2rec("QCDdata"+'.root',"T").diTauNSVfitMass, bins);
for i in range(0, len(hqcdw)):
    hist, bins =  np.histogram(hqcd[i], bins, weights=hqcdw[i]);
    histqcd = histqcd - weighttableqcd[i]*hist;

'''
hsum = 0;
for i in range(0, len(hqcdw)):
    hist, bins =  np.histogram(hqcd[i], bins, weights=hqcdw[i]);
    hsum = hsum +  (weighttableqcd[i]*hist).sum();

histqcd, bins =  np.histogram(root2rec("QCDdata"+'.root',"T").diTauNSVfitMass, bins, density=1);
'''
histqcd = 1.06*histqcd;
#histqcd = 1.06*hsum*histqcd*bin_width;
print histqcd.sum()
#histqcd = 0*histqcd;

plt.bar(bins[:-1], histqcd, width=bin_width,  color="#FF80FF",  alpha=1, linewidth=1,  label='qcd')


MChist = [];
for i in range(0,len(h)):
    hist, bins = np.histogram(h[i], bins, weights=hw[i]);
    MChist.append(hist);

histsum=histqcd;
for i in range(0,len(MChist)):
    print MChist[i].sum()
    plt.bar(bins[:-1], MChist[i], width=bin_width,  color=kolor[i],  alpha=1, linewidth=1,  label=legenda[i], bottom=histsum)
    histsum = histsum + MChist[i];



counts, bins, bars =  plt.hist(hdata, bins ,  linewidth=0 , alpha=0 ,normed=0 )
dataERROR = np.sqrt(counts);
plt.plot(bins[:-1] + bin_width2, counts, 'o', markersize=10, color='black', label='Observed')
#plt.plot(bins[:-1] + (bin_width+0.)/2, counts, 'o', markersize=10 ,color='black', label='Observed')
#plt.errorbar( bins[:-1] + (bin_width+0.)/2, counts,yerr=dataERROR, fmt=None,color='black')
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend([handles[0], handles[9], handles[7], handles[3], handles[2], handles[1] ], [labels[0], labels[9], labels[7], labels[3], labels[2], labels[1]])
#plt.legend(handles[::-1], labels[::-1])
ax1.set_xlabel('SVfit mass (GeV)')
ax1.set_ylabel('Events')

ax2  = plt.subplot(gs[7, :])

po = np.divide(np.array(counts-histsum, dtype=float), np.array(histsum, dtype=float))
plt.plot(bins[:-1] + bin_width2, po, 'o', color='black', label='Efficiency')
plt.axhline(y=0, linestyle='-', color='red', linewidth=2, zorder=2)
ax2.set_ylabel(r'$\frac{{DATA - MC}}{MC}$')
plt.ylim([-3,3])
plt.xlim([0,400])

plt.draw()
plt.show()


'''
plt.hist(h[1], bins , stacked=1,  linewidth=0 , alpha=1, weights=hw[1] ,normed=0, color=kolor[1] )
plt.hist(h[2], bins , stacked=1,  linewidth=0 , alpha=1, weights=hw[2] ,normed=0, color=kolor[2] )
plt.hist(h[3], bins , stacked=1,  linewidth=0 , alpha=1, weights=hw[3] ,normed=0, color=kolor[3] )
plt.hist(h[4], bins , stacked=1,  linewidth=0 , alpha=1, weights=hw[4] ,normed=0, color=kolor[4] )
plt.hist(h[5], bins , stacked=1,  linewidth=0 , alpha=1, weights=hw[5] ,normed=0, color=kolor[5] )
#bins=np.arange(0,350,bin_width) 
#histdata, bins =  np.histogram(hdata, bins ) # , normed=1);
#plt.bar(bins[:-1], histdata, width=bin_width ,edgecolor='black' ,  alpha=0.5, color="#809980", linewidth=2, ls='dotted', label='L1', hatch="o"  )
'''
#plt.bar(bins[:-1], histdata, width=bin_width ,edgecolor='black' ,  alpha=0, linewidth=2, ls='dotted', label='L1', hatch="o"  )
#plt.hist(hdata, bins , linewidth=1 , alpha=1,normed=0, color="black")
