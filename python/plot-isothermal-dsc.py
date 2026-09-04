import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch

# Column shorthands
t = 'Time (min)'
T = 'Temperature (°C)'
H = 'Heat Flow (W/g)'

# Folders
data_folder = '../clean/dsc/conventional/'
imgs_folder = '../images/'

# Cooling rate vs. degree of crystallinity
fn = 'isothermal-155C-2hrs.csv'
df_155 = pd.read_csv(data_folder + fn,
                  header=1, names=[t, T, H])
fn = 'isothermal-177C-2hrs.csv'
df_177 = pd.read_csv(data_folder + fn,
                  header=1, names=[t, T, H])

# Bounds
iso_155 = [8700, 79750]
iso_177 = [9950, 81100]
ht_155 = [80000, 93600]
ht_177 = [81320, 93600]

# Offset for plotting
ΔH_iso = 0.0003
ΔH_ht = 0.05

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


# Plot isothermal data
f, ax = plt.subplots(figsize=fsize)
ax.set_position(apos)
ax.plot(df_155[t][iso_155[0]:iso_155[1]] - df_155[t][iso_155[0]],
        df_155[H][iso_155[0]:iso_155[1]],
        color='#555555', linewidth=1,
        label="155 °C")
ax.plot(df_177[t][iso_177[0]:iso_177[1]] - df_177[t][iso_177[0]],
        df_177[H][iso_177[0]:iso_177[1]] + ΔH_iso,
        color='#999999', linewidth=1,
        label='177 °C')

ax.set_xlabel('time [min.]')
ax.set_ylabel('normalized heat flow [W/g]')
ax.set_xlim((-2, 122))
ax.set_ylim((-.0065, -0.002))
ax.set_xticks([0, 30, 60, 90, 120])
ax.set_yticks([])
ax.legend(frameon=False)

patch = FancyArrowPatch(
    posA=(4, -0.0022), posB=(4, -0.0027),
    arrowstyle='|-|', mutation_scale=2, linewidth=0.5, color='black')
ax.add_patch(patch)
ax.text(7, -0.00255, '0.5 mW/g')

ax.plot([10, 110], [-0.005, -0.005], '--', lw=0.75, color='#999999')
ax.text(51, -0.0045, 'crystallization\npeak', ha='center')
plt.savefig(imgs_folder + 'cure-isothermal.pdf')
plt.show()

# Plot subsequent heating trace
f, ax = plt.subplots(figsize=fsize)
ax.set_position(apos)
ax.plot(df_155[T][ht_155[0]:ht_155[1]],
        df_155[H][ht_155[0]:ht_155[1]],
        color='#555555', linewidth=1,
        label="155 °C")
ax.plot(df_177[T][ht_177[0]:ht_177[1]],
        df_177[H][ht_177[0]:ht_177[1]] + ΔH_ht,
        color='#999999', linewidth=1,
        label='177 °C')

ax.set_xlabel('temperature [°C]')
ax.set_ylabel('normalized heat flow [W/g]')
ax.set_xlim((140, 401))
ax.set_yticks([])
ax.legend(frameon=False, loc='lower left')

patch = FancyArrowPatch(
    posA=(325, -0.06), posB=(325, -0.11),
    arrowstyle='|-|', mutation_scale=2, linewidth=0.5, color='black')
ax.add_patch(patch)
ax.text(331, -0.094, '50 mW/g')

ax.text(280, -0.17, 'crystallization\npeak', ha='center')
ax.plot([215, 230], [-0.137, -0.137], color='black', lw=0.5)
plt.savefig(imgs_folder + 'cure-ht.pdf')
plt.show()
