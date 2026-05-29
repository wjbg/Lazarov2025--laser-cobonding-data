import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Column shorthands
CR = 'Cooling rate (K/s)'
Xc = 'DoC (%)'

# Folders
data_folder = '../clean/dsc/'
imgs_folder = '../images/'

# Cooling rate vs. degree of crystallinity
fn = 'coolingrate-vs-doc.csv'
DoC = pd.read_csv(data_folder + fn,
                  header=1, names=[CR, Xc, 'type'])

# Plot settings
fsize = (3.1, 2.7)
apos = [0.18, 0.18, 0.74, 0.76]
font = {'family' : 'serif',
        'serif'  : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 9}
matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'


# Plot data
f, ax = plt.subplots(figsize=fsize)
ax.set_position(apos)

ax.semilogx(DoC[DoC['type']=='DSC'][CR],
            DoC[DoC['type']=='DSC'][Xc]/100,
            ls='', marker='s', mfc='#999999', mec='black', ms=5)
ax.semilogx(DoC[DoC['type']=='fDSC'][CR],
            DoC[DoC['type']=='fDSC'][Xc]/100,
            ls='', marker='o', mfc='#555555', mec='black', ms=5)

ax.set_xlabel('cooling rate [°C/s]')
ax.set_ylabel('degree of crystallinity [-]')
ax.set_ylim((0, 0.2))
ax.set_yticks(np.linspace(0, 0.2, 5))
ax.legend([Line2D([0], [0],
                  ls='', marker='s', mfc='#999999', mec='black', ms=5),
           Line2D([0], [0],
                  ls='', marker='o', mfc='#555555', mec='black', ms=5)],
          ['DSC', 'Flash DSC'],
          frameon=False)
ax.plot([10, 10], [0.015, 0.03], ':', lw=0.5, color='black')
ax.text(8, 0.032, r'$\dot{T}_\mathrm{c}$')
plt.savefig(imgs_folder + 'coolingrate-vs-doc.pdf')
plt.show()
