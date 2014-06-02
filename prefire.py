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
    for j in xrange(0,len(rec)):
        if (rec.Tlbx_1[j]):
            print "Tlbx0: ", rec.Tlbx0[j], "Pt0: ", rec.TptT0[j], "Pt_1", rec.TptT_1[j],  "Eta:", rec.Teta0[j], "Phi:", rec.Tphi0[j], "Quality w bx=-1:", rec.Tquality_1[j], "Qual w BX = 0:", rec.Tquality0[j], " Tsize", rec.Tsize0[j];
    
