import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


# Column shorthands
T = 'Temperaturee (°C)'
H = 'Heat flow (W/g)'

# Folder
data_folder = '../clean/dsc/laser-sample/'
imgs_folder = '../imgs/'

# Load file
fn = 'heating-trace.csv'
df = pd.read_csv(data_folder + fn, header=1, names=[T, H])

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
ax.plot(df[df[T]>100][T], df[df[T]>100][H], 'k', lw=1)
ax.set_yticks([])
ax.set_xlabel('temperature [°C]')
ax.set_ylabel('normalized heat flow [W/g]')

patch = FancyArrowPatch(
    posA=(100, -0.15), posB=(100, -0.20),
    arrowstyle='|-|', mutation_scale=2, linewidth=0.5, color='black')
ax.add_patch(patch)
ax.text(105, -0.18, '0.5 W/g')
# plt.savefig(imgs_folder + 'dsc-laser-sample.pdf')
plt.show()
