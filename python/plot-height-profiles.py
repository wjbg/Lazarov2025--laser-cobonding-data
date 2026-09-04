import matplotlib
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Folders
data_folder = '../clean/confocal/'
imgs_folder = '../images/'

# Load data
bmp_fns = ['reference-1.bmp', 'treated-1.bmp', 'annealed-1.bmp']
bitmaps = [Image.open(data_folder + fn) for fn in bmp_fns]

fns = ['reference-1.csv', 'treated-1.csv', 'annealed-1.csv']
height = [np.loadtxt(data_folder + fn,
                     delimiter=',',
                     skiprows=49,
                     quotechar='"') for fn in fns]

# Resolution for: [reference, treated, annealed]
Δxy = [276E-3, 276E-3, 284E-3]  # μm / pixel
Δz = [1E-3, 1E-3, 1E-3]  # μm / pixel

# Center the height data and convert to μm, also flip to comply with bitmap
height[0] = np.flipud((height[0] - height[0].mean()) * Δz[0])
height[1] = np.flipud((height[1] - height[1].mean()) * Δz[1])
height[2] = np.flipud((height[2] - height[2].mean()) * Δz[2])

cmin = min(h.min() for h in height)
cmax = max(h.max() for h in height)
cmin = -15.0
cmax = 15.0
levels = np.linspace(cmin, cmax, 21)


# Plot settings
fsize = (5.5, 4.1)
font = {'family' : 'serif',
        'serif'  : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 9}
matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

# Plot data
f = plt.figure(figsize=fsize)

gs = GridSpec(
    2, 3,
    figure=f,
    left=0.05,
    right=0.95,
    top=0.95,
    bottom=0.18,
    wspace=0.20,
    hspace=0.10)

labels = ['Reference', 'Treated', 'Annealed']

for i, bm in enumerate(bitmaps):
    ax = f.add_subplot(gs[0, i])
    ax.imshow(bm)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(labels[i], fontsize=9)

for i, h in enumerate(height):
    ax = f.add_subplot(gs[1, i])
    ax.set_rasterization_zorder(1)
    cf = ax.contourf(h,
                     levels=levels,
                     vmin=cmin,
                     vmax=cmax,
                     cmap="Greys_r",
                     zorder=0)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])


# Color bar
cbar_ax = f.add_axes([
    0.25,   # left
    0.12,   # bottom
    0.50,   # width
    0.025   # height
])

cbar = f.colorbar(cf, cax=cbar_ax, orientation="horizontal")
cbar.set_label(r"height [\textmu m]")

plt.savefig(imgs_folder + 'surface-plots.pdf', dpi=300)
plt.show()
