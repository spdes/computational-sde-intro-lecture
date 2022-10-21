"""
Generate realisations of Brownian motion.
"""
import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
T = 10000
ts = np.linspace(dt, dt * T, T)

np.random.seed(666)

num_samples = 10

# Set plotting parameters
plt.rcParams.update({
    'text.usetex': True,
    'font.family': "serif",
    'text.latex.preamble': r'\usepackage{amsmath,amsfonts}',
    'font.serif': ["Computer Modern Roman"],
    'font.size': 20})

for i in range(num_samples):
    dws = np.sqrt(dt) * np.random.randn(T, )
    ws = np.cumsum(dws)

    plt.plot(ts, ws, linewidth=0.5)

# Plot 0.95 interval
plt.fill_between(ts,
                 -1.96 * np.sqrt(ts),
                 1.96 * np.sqrt(ts),
                 color='black',
                 edgecolor='none',
                 alpha=0.15,
                 label='0.95 quantile')

plt.xlabel('$t$')
plt.ylabel('$W(t)$')
plt.grid(linestyle='--', alpha=0.3, which='both')

plt.legend()

plt.tight_layout(pad=0.1)
plt.show()
