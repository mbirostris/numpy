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
from matplotlib.colors import LogNorm

pp = PdfPages('multipage.pdf')

plik=str(sys.argv[1]);

try:
    os.mkdir("./rysunki/")
except:
    print "Jedziemyyyy...."

#z reki
#pliki=["ot001", "ot002", "ot009", "ot019", "ot020" , "nt001"]; 





bin_width = 0.01;
rec = root2rec(sys.argv[1], "tdig")
       
#x = np.extract(np.absolute(rec.Teta) < 1.61, rec.Tbeta)
#x = np.extract(np.logical_and(np.logical_and(np.absolute(rec.Teta0) < 1.61, rec.Tlbx_1), rec.Tpt0 > 10), rec.Teta0);
#y = np.extract(np.logical_and(np.logical_and(np.absolute(rec.Teta0) < 1.61, rec.Tlbx_1), rec.Tpt0 > 10), rec.Tphi0);

for i in range(0, len(rec)):
    print i
'''
print  len(x), len(y)

pl.hist2d(x, y, bins=200, norm=LogNorm())
#pl.hist2d(x, y, bins=np.arange(0.,4,bin_width) , norm=LogNorm())
pl.colorbar()
#plt.xscale('log')
plt.ylabel(r'$\phi$')
plt.xlabel(r'$\eta$')
plt.draw()
pp.savefig()
pp.close()
plt.show()
'''
