import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Column shorthands
δ = 'displacement (mm)'
G = 'toughness, (kJ/m2)'

# Folders
data_folder = '../clean/peel/'
imgs_folder = '../images/'

# Load data
fn_ref = ['reference-1.csv', 'reference-2.csv', 'reference-3.csv',
          'reference-4.csv', 'reference-5.csv']
fn_tre = ['treated-1.csv', 'treated-2.csv', 'treated-3.csv',
          'treated-4.csv', 'treated-5.csv']

data_ref = [pd.read_csv(data_folder + fn, sep=';', header=1, names=[δ, G]) for fn in fn_ref]
data_tre = [pd.read_csv(data_folder + fn, sep=';', header=1, names=[δ, G]) for fn in fn_tre]

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

# Example curves
if True:
    f, ax = plt.subplots(figsize=fsize)
    ax.set_position(apos)
    ax.plot(data_tre[3][δ], data_tre[3][G], lw=1, color='#555555', label='Treated')
    ax.plot(data_ref[3][δ]-5, data_ref[3][G], lw=1, color='#999999', label='Reference')

    ax.set_xlabel(r'displacement [mm]')
    ax.set_ylabel(r'fracture toughness [kJ/m$^2$]')
    ax.set_ylim((0, 1.0))
    ax.set_xlim((0, 60))
    ax.legend(frameon=False)
    plt.savefig(imgs_folder + 'disp-vs-toughness-example.pdf')
    plt.show()


# Average + std
Δ = (30, 50)
G_ref = np.array([df[(df[δ]>Δ[0]) & (df[δ]<Δ[1])][G].mean() for df in data_ref])
G_tre = np.array([df[(df[δ]>Δ[0]) & (df[δ]<Δ[1])][G].mean() for df in data_tre])

if True:
    f, ax = plt.subplots(figsize=fsize)
    ax.set_position(apos)
    ax.bar([1, 2], [G_tre.mean(), G_ref.mean()],
           yerr=[G_tre.std(), G_ref.std()], capsize=8,
           facecolor=["#555555", "#999999"],
           edgecolor=["black", "black"])
    ax.set_xticks([1, 2])
    ax.set_xticklabels(['Treated', 'Reference'])
    ax.set_xlim((0.25, 2.75))
    ax.set_ylim((0, 0.5))
    ax.set_ylabel('fracture toughness [kJ/m$^2$]')
    plt.savefig(imgs_folder + 'average-toughness.pdf')
    plt.show()
