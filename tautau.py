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
import HistMacro as mac

try:
    os.mkdir("./rysunki/"+plik)
except:
    print "Jedziemyyyy...."

def page(category):
    fig = plt.figure(figsize=(16, 16))
    plt.axis([0, 10, 0, 10])
    plt.text(5, 7, "Kategoria:\n" + category , fontsize=50,color='b', ha='center', va='top')
    return fig;
    

category = ['Inclusive', 'MtLeg1MVA']; # variable = ["MtLeg1MVA"]; bin_width = [1]; bin_min=[0]; bin_max=[150]

variable = ["diTauVisMass","diTauNSVfitMass","visibleTauMass", "decayMode", "MEtMVA", "MEtMVAPhi", "MtLeg1MVA", "ptL1", "ptL2", "etaL1", "etaL2", "phiL1", "phiL2", "pt1", "pt2", "eta1", "eta2", "phi1", "phi2", "Deta", "Dphi", "Mjj", "diTauRecoPt", "numPV"];
bin_width = [4.0, 6.0, 0.05, 0.1, 4.0, 0.1, 2.0, 2.0,2.0, 0.1, 0.1, 0.1, 0.1,4.0 ,4.0, 0.4, 0.4, 0.4, 0.4, 0.4,0.4, 8.0,4.0,1.0]; 
bin_min   = [0,   0,   0,   -0.1, 0,  -3.3, 0  , 0 , 0  ,-2.2,-2.2,-3.3,-3.3, 0  ,0  ,-6,-6,-5,-5,-2,0,             0 ,  0  ,0  ]; 
bin_max   = [204, 356, 2.01, 2.3, 204, 3.3, 150 ,150,150, 2.2, 2.2, 3.3, 3.3,250,250, 7, 7, 5, 5, 9, 5,     500,  250,50 ];



#bins=[0., 20., 40., 60., 80., 100., 120., 140., 160., 180., 200., 250., 300., 350. ];
#bins=[0., 10.,  20., 30.,  40., 50.,  60., 70., 80.,90.,  100.,110., 120.,130., 140.,150., 160.,170., 180.,190., 200.,225., 250.,275., 300., 350. ];
#bins=np.arange(bin_min,bin_max,bin_width) 
pp = PdfPages('analysis.pdf')
for j in xrange(0, len(category)):
    fih = page( category[j])
    pp.savefig(fih)
    for i in xrange(0, len(variable)):
        if (category[j] == 'MtLeg1MVA' and variable[i] != 'MtLeg1MVA'):
            continue
        fig = mac.plot(variable[i], category[j], np.arange(bin_min[i],bin_max[i],bin_width[i]) )
        pp.savefig(fig)
        plt.close()

pp.close()
