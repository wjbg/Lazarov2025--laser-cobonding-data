import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Column shorthands
δ = 'Distance (µm)'
Br = 'Br L series'
Br_s = 'Br L series - smooth'

# Folders
data_folder = '../clean/edx/'
imgs_folder = '../images/'

# Load data
fns = ['edx-reference-1.csv', 'edx-reference-2.csv', 'edx-reference-3.csv']
reference = [pd.read_csv(data_folder + fn, index_col=0) for fn in fns]

fns = ['edx-treated-1.csv', 'edx-treated-2.csv', 'edx-treated-3.csv']
treated = [pd.read_csv(data_folder + fn, index_col=0) for fn in fns]

# Smooth data
width = 10  # smoothing window width
for i in range(3):
    reference[i][Br_s] = reference[i][Br].rolling(window=width).mean()
    treated[i][Br_s] = treated[i][Br].rolling(window=width).mean()

# Offset to center the graphs -- determined through eyeballing
Δref = [3.257, 2.778, 2.619]
Δtre = [3.443, 2.573, 2.858]


for i in range(3):
    reference[i][δ] = reference[i][δ] - Δref[i]
    treated[i][δ] = treated[i][δ] - Δtre[i]

# Determine normalization value from Br content for x < -0.5
xlim = -0.5
Br_ref = [None]*3
Br_tre = [None]*3

for i in range(3):
    Br_ref[i] = reference[i][Br][reference[i][δ] < xlim].mean()
    Br_tre[i] = treated[i][Br][treated[i][δ] < xlim].mean()

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

for i in range(3):
    ax.plot(treated[i][δ],
            treated[i][Br_s]/Br_tre[i],
            color='#555555', linewidth=1)
    ax.plot(reference[i][δ],
            reference[i][Br_s]/Br_ref[i],
            color='#999999', linewidth=1)

ax.legend([Line2D([0], [0], color='#555555', linewidth=1),
           Line2D([0], [0], color='#999999', linewidth=1)],
          ['Treated (3x)', 'Reference (3x)'],
          frameon=False)
ax.set_xlabel(r'distance [\textmu m]')
ax.set_ylabel('normalized bromine count [-]')
plt.savefig(imgs_folder + 'bromine-edx.pdf')
plt.show()
