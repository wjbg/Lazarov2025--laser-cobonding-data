import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Column shorthands
λ = 'Wavenumber (cm-1)'
I = 'Intensity'

# Folders
data_folder = '../clean/ftir/'
imgs_folder = '../images/'

# Load data
fn = 'ftir-reference.csv'
reference = pd.read_csv(data_folder + fn)

fn = 'ftir-laser-heated.csv'
treated = pd.read_csv(data_folder + fn)

# Normalization by value at 1588 cm-1
reference[I] = reference[I]/reference[I][1025]
treated[I] = treated[I]/treated[I][1025]

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
ax.invert_xaxis()

ax.plot(treated[λ],
        treated[I],
        label='Treated',
        color='#555555', linewidth=1)
ax.plot(reference[λ],
        reference[I],
        label='Reference',
        color='#999999', linewidth=1)


ax.legend(frameon=False)

ax.set_xlabel(r'wavenumber [cm$^{-1}$]')
ax.set_ylabel('normalized intensity [-]')

ax.set_xlim([1800, 600])

plt.savefig(imgs_folder + 'ftir.pdf')
plt.show()
