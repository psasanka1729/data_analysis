import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from math import pi
X,Y,W = np.loadtxt('plot_data_12_7000.txt', delimiter = '\t', unpack=True)
x = X.tolist()
y = Y.tolist()
w = W.tolist()
font = {#'family' : 'Helvetica',
        #'weight' : 'bold',
        'size'   : 60}

plt.rc('font', **font)
# use a gray background
plt.rcParams['axes.facecolor'] = 'white'
#plt.rcParams['axes.grid'] = 'True'

f = plt.figure()
f.set_figwidth(35)
f.set_figheight(25)
plt.scatter(x, y, c=w, cmap='autumn', s=4, label = '')
plt.xlabel("Noise $\delta$")
plt.ylabel("Energy $\phi_{F}$")
plt.title("L=12, Page value = 3.66, Seed = 7000")

plt.yticks([-pi, -pi/2, -3*pi/4, -pi/4, 0, pi/4, 3*pi/4, pi/2, pi],
           ['$-\pi$', r'$-\pi/2$', r'$-3\pi/4$', r'$-\pi/4$', r'$0$', r'$\pi/4$', r'$3\pi/4$',
            r'$\pi/2$', '$\pi$' ])

plt.axhline(y=3.11034138188, color='k', linestyle='-',linewidth = 2)
plt.axhline(y=-3.11034138188, color='k', linestyle='-',linewidth = 2)
plt.axhline(y=0, color='k', linestyle='-',linewidth = 2)
plt.xlim([0, 0.4])
plt.ylim([-np.pi-0.1, np.pi+0.1])

plt.colorbar(orientation="vertical")#.set_label(label='Average Entanglement Entropy',size=30,weight='bold')
plt.savefig('energy_noise_12_7000.png', dpi=100, bbox_inches='tight')