import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch

# Column shorthands
Ts = 'Sample temperature (C)'
Hf = 'Heat flow (mW)'

# Folders
data_folder = '../clean/dsc/flash-dsc/'
imgs_folder = '../images/'

fns = ["001K-per-s.csv",
       "002K-per-s.csv",
       "003K-per-s.csv",
       "007K-per-s.csv",
       "010K-per-s.csv",
       "020K-per-s.csv",
       "025K-per-s.csv",
       "050K-per-s.csv",
       "100K-per-s.csv",
       "150K-per-s.csv"]

data = [pd.read_csv(data_folder + fn, header=1, names=[Ts, Hf]) for fn in fns]
cr_labels = ['1 °C/s', '2 °C/s', '3 °C/s', '7.5 °C/s', '10 °C/s',
             '20 °C/s', '25 °C/s', '50 °C/s', '100 °C/s', '150 °C/s']

# Plot settings
fsize = (3.1, 2.7)
apos = [0.18, 0.18, 0.74, 0.76]
font = {'family' : 'serif',
        'serif'  : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 9}
matplotlib.rc('font', **font)

# colors = plt.cm.cividis(np.linspace(0, 1, 10))
colors = plt.cm.gray(np.linspace(0.15, 0.7, 10))

# Plot data
f, ax = plt.subplots(figsize=fsize)
ax.set_position(apos)

for i, df in enumerate(data):
    ax.plot(df[df[Ts]>120][Ts],
            df[df[Ts]>120][Hf],
            linewidth=1, color=colors[i], label=cr_labels[i])

# ax.set_yticks([])
ax.set_ylabel('normalized heat flow [mW]')
ax.set_xlabel('temperature [°C]')
ax.set_xlim((100, 400))
ax.set_xticks(np.linspace(100, 400, 4))
ax.set_yticks([])
ax.legend(frameon=False, loc='lower left',
          labelspacing=0.1, handletextpad=0.2, handlelength=1.0)

patch = FancyArrowPatch(
    posA=(380, -1.35),
    posB=(380, -1.55),
    arrowstyle='|-|',       # <--- bars on both ends
    mutation_scale=2,      # size of the bars
    linewidth=0.5,
    color='black')
ax.add_patch(patch)
ax.text(375, -1.48, '0.2 mW', ha='right')
# plt.savefig(imgs_folder + 'fDSC-cooling-rates.pdf')
plt.show()
