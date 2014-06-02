import numpy as np
import itertools as IT
import matplotlib.pyplot as plt
N = 50
nbin = 10

xs = [np.array([i,i,i+1,i+1]) for i in range(N)]
ys = [np.array([i,i+1,i,i+1]) for i in range(N)]
masses = np.arange(N)

heatmap = 0
xedges = np.linspace(0, N, nbin)
yedges = np.linspace(0, N, nbin)

for x, y, mass in IT.izip(xs, ys, masses):
    hist, xedges, yedges = np.histogram2d(
        x, y, bins=[xedges, yedges], weights=None)
#        x, y, bins=[xedges, yedges], weights=np.ones_like(x)*mass)
    heatmap += hist

extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
heatmap = np.flipud(np.rot90(heatmap))
fig, ax = plt.subplots()
ax.imshow(heatmap, extent=extent, interpolation='nearest')
plt.show()
