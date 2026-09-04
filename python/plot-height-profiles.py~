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

fns = ['edx-annealed-1.csv', 'edx-annealed-2.csv', 'edx-annealed-3.csv']
annealed = [pd.read_csv(data_folder + fn, index_col=0) for fn in fns]

# Smooth data
width = 10  # smoothing window width
for i in range(3):
    reference[i][Br_s] = reference[i][Br].rolling(window=width).mean()
    treated[i][Br_s] = treated[i][Br].rolling(window=width).mean()
    annealed[i][Br_s] = annealed[i][Br].rolling(window=width).mean()


# Offset to center the graphs -- determined through eyeballing
Δref = [3.257, 2.778, 2.619]
Δtre = [3.443, 2.573, 2.858]
Δann = [3.164, 3.110, 3.192]

for i in range(3):
    reference[i][δ] = reference[i][δ] - Δref[i]
    treated[i][δ] = treated[i][δ] - Δtre[i]
    annealed[i][δ] = annealed[i][δ] - Δann[i]

# Determine normalization value from Br content for x < -0.5
xlim = -0.5
Br_ref = [None]*3
Br_tre = [None]*3
Br_ann = [None]*3

for i in range(3):
    Br_ref[i] = reference[i][Br][reference[i][δ] < xlim].mean()
    Br_tre[i] = treated[i][Br][treated[i][δ] < xlim].mean()
    Br_ann[i] = annealed[i][Br][annealed[i][δ] < xlim].mean()

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
ax.plot([0.0, 0.0], [0.0, 1.1], '--', color='black', linewidth=0.5)

for i in range(3):
    ax.plot(treated[i][δ],
            treated[i][Br_s]/Br_tre[i],
            color='#555555', linewidth=1)
    ax.plot(reference[i][δ],
            reference[i][Br_s]/Br_ref[i],
            color='#999999', linewidth=1)
    ax.plot(annealed[i][δ],
            annealed[i][Br_s]/Br_ann[i],
            linestyle=(0, (10, 25)), color='#3A3A3A', linewidth=1)

ax.legend([Line2D([0], [0], color='#555555', linewidth=1),
           Line2D([0], [0], color='#999999', linewidth=1),
           Line2D([0], [0], linestyle='--', color='#3A3A3A', linewidth=1)],
          ['Treated (3x)', 'Reference (3x)', 'Annealed (3x)'],
          frameon=False)
ax.set_xlabel(r'distance [\textmu m]')
ax.set_ylabel('normalized bromine count [-]')
ax.text(-2.0, 0.5, r'FM300', ha='center')
ax.text(5.0, 0.5, r'C/PEKK', ha='center')
plt.savefig(imgs_folder + 'bromine-edx.pdf')
plt.show()
