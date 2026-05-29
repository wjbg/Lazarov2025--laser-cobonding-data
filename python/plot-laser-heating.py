import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Column shorthands
t = 'Time (s)'
T = 'Temperature (°C)'

# Folders
data_folder = '../clean/static-laser-heating/'
imgs_folder = '../images/'

# Load data
fn05 = ['225W-0500ms.csv', '250W-0500ms.csv', '275W-0500ms.csv', '300W-0500ms.csv',
        '325W-0500ms.csv', '350W-0500ms.csv', '375W-0500ms.csv', '400W-0500ms.csv',
        '425W-0500ms.csv']
fn10 = ['100W-1000ms.csv', '125W-1000ms.csv', '150W-1000ms.csv', '175W-1000ms.csv',
        '200W-1000ms.csv', '225W-1000ms.csv', '250W-1000ms.csv', '275W-1000ms.csv',
        '300W-1000ms.csv', '325W-1000ms.csv', '350W-1000ms.csv']

data_05 = [pd.read_csv(data_folder + fn, header=0, names=[t, T]) for fn in fn05]
data_10 = [pd.read_csv(data_folder + fn, header=0, names=[t, T]) for fn in fn10]
power_05 = np.linspace(225, 425, 9, endpoint=True, dtype=int)
power_10 = np.linspace(100, 350, 11, endpoint=True, dtype=int)

# Filter to only include max T > 270
df05 = []
df10 = []
P05 = []
P10 = []

T_filter = 270
for i, df in enumerate(data_05):
    if df[T].max() > T_filter:
        df05.append(df)
        P05.append(power_05[i])

for i, df in enumerate(data_10):
    if df[T].max() > T_filter:
        df10.append(df)
        P10.append(power_10[i])

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


# Plot data for t = 0.5 s
col05 = plt.cm.gray(np.linspace(0.1, 0.7, len(df05)))[::-1]
if True:
    f, ax = plt.subplots(figsize=fsize)
    ax.set_position(apos)

    for i, df in enumerate(df05[::-1]):
        ax.plot(df[t], df[T],
                lw=1, color=col05[i], label=str(P05[::-1][i]) + ' W')

    ax.set_xlabel('time [s]')
    ax.set_xlim((0, 5))
    ax.set_ylim((50, 550))
    ax.set_ylabel('surface temperature [°C]')
    ax.legend(frameon=False, loc='upper right',
              labelspacing=0.1, handletextpad=0.2, handlelength=1.0)
    ax.plot([0, 1.0], [337, 337], ':k', lw=0.5)
    ax.text(1.1, 324, r'$T_\mathrm{m}$')
    plt.savefig(imgs_folder + 't-vs-T-500ms.pdf')
    plt.show()


# Plot data for t = 1.0 s
col10 = plt.cm.gray(np.linspace(0.1, 0.7, len(df10)))[::-1]
if True:
    f, ax = plt.subplots(figsize=fsize)
    ax.set_position(apos)

    for i, df in enumerate(df10[::-1]):
        ax.plot(df[t], df[T],
                lw=1, color=col10[i], label=str(P10[::-1][i]) + ' W')

    ax.set_xlabel('time [s]')
    ax.set_xlim((0, 5))
    ax.set_ylim((50, 550))
    ax.set_ylabel('surface temperature [°C]')
    ax.legend(frameon=False, loc='upper right',
              labelspacing=0.1, handletextpad=0.2, handlelength=1.0)
    ax.plot([0, 1.7], [337, 337], ':k', lw=0.5)
    ax.text(1.8, 324, r'$T_\mathrm{m}$')
    plt.savefig(imgs_folder + 't-vs-T-1000ms.pdf')
    plt.show()

# Maximum temperatures
Tmax05 = np.array([df[T].max() for df in df05])
Tmax10 = np.array([df[T].max() for df in df10])

if True:
    f, ax = plt.subplots(figsize=fsize)
    ax.set_position(apos)

    ax.plot(P05, Tmax05,
             ls='', marker='s', mfc='#999999', mec='black', ms=5)
    ax.plot(P10, Tmax10,
            ls='', marker='o', mfc='#555555', mec='black', ms=5)

    ax.set_xlabel('power [W]')
    ax.set_ylabel('max. surface temperature [°C]')
    ax.legend([Line2D([0], [0],
                  ls='', marker='s', mfc='#999999', mec='black', ms=5),
           Line2D([0], [0],
                  ls='', marker='o', mfc='#555555', mec='black', ms=5)],
          [r'$\Delta t$ = 0.5 s', r'$\Delta t$ = 1.0 s'],
          frameon=False, loc='upper left',
          labelspacing=0.1, handletextpad=0.2, handlelength=1.0)
    ax.set_xlim((150, 500))
    ax.set_ylim((225, 550))
    ax.plot([150, 500], [337, 337], ':k', lw=0.5)
    ax.text(160, 343, r'$T_\mathrm{m}$')
    plt.savefig(imgs_folder + 'P-vs-maxT.pdf')
    plt.show()

# Cooling rates
T_int = (220, 240)
CR05 = np.zeros_like(Tmax05)
CR10 = np.zeros_like(Tmax10)

for i, df in enumerate(df05):
    idx = (df[T] < T_int[1]) & (df[T] > T_int[0]) & (df[t] > 0.5)
    CR05[i] = np.polyfit(df[t][idx], df[T][idx], 1)[0]

for i, df in enumerate(df10):
    idx = (df[T] < T_int[1]) & (df[T] > T_int[0]) & (df[t] > 1.0)
    CR10[i] = np.polyfit(df[t][idx], df[T][idx], 1)[0]

if True:
    f, ax = plt.subplots(figsize=fsize)
    ax.set_position(apos)

    ax.plot(P05, -CR05,
             ls='', marker='s', mfc='#999999', mec='black', ms=5)
    ax.plot(P10, -CR10,
            ls='', marker='o', mfc='#555555', mec='black', ms=5)

    ax.set_xlabel('power [W]')
    ax.set_ylabel('cooling rate at 250 °C [°C/s]')
    ax.legend([Line2D([0], [0],
                  ls='', marker='s', mfc='#999999', mec='black', ms=5),
           Line2D([0], [0],
                  ls='', marker='o', mfc='#555555', mec='black', ms=5)],
          [r'$\Delta t$ = 0.5 s', r'$\Delta t$ = 1.0 s'],
          frameon=False, loc='upper right',
          labelspacing=0.1, handletextpad=0.2, handlelength=1.0)
    ax.set_xlim((150, 500))
    ax.set_ylim((0, 575))
    ax.plot([150, 500], [10, 10], ':k', lw=0.5)
    ax.text(160, 18, r'$\dot{T}_\mathrm{c}$')
    plt.savefig(imgs_folder + 'P-vs-cooling-rate.pdf') #
    plt.show()
