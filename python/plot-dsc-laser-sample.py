import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


# Column shorthands
T = 'Temperature (°C)'
H = 'Heat flow (W/g)'

# Folder
data_folder = '../clean/dsc/laser-sample/'
imgs_folder = '../images/'

# Load data
fn = 'treated.csv'
tre = pd.read_csv(data_folder + fn, header=1, names=[T, H])

fn = 'annealed.csv'
ann = pd.read_csv(data_folder + fn, header=1, names=[T, H])

ΔH = -0.15  # Offset for plotting annealed curve

# Plot settings
fsize = (3.1, 2.7)
apos = [0.18, 0.18, 0.74, 0.76]
font = {'family' : 'serif',
        'serif'  : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 9}
matplotlib.rc('font', **font)

# Plot data
f, ax = plt.subplots(figsize=fsize)
ax.set_position(apos)
ax.plot(tre[tre[T]>100][T], tre[tre[T]>100][H], '#999999', lw=1, label='Treated')
ax.plot(ann[ann[T]>100][T], ann[ann[T]>100][H] + ΔH, '#3A3A3A', lw=1, label='Annealed')
ax.set_yticks([])
ax.set_xlabel('temperature [°C]')
ax.set_ylabel('normalized heat flow [W/g]')

patch = FancyArrowPatch(
    posA=(100, -0.15), posB=(100, -0.20),
    arrowstyle='|-|', mutation_scale=2, linewidth=0.5, color='black')
ax.add_patch(patch)
ax.text(105, -0.185, '50 mW/g')
ax.legend(frameon=False)
plt.savefig(imgs_folder + 'dsc-laser-sample.pdf')
plt.show()
