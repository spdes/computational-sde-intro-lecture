"""
A computational introduction to stochastic differential equations.

Lecture 3.

https://github.com/spdes/computational-sde-intro-lecture.

Simulating a modified Duffing--van der Pol SDE using Euler--Maruyama.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(666)

alpha = 2


def drift(x):
    return np.array([x[1],
                     x[0] * (alpha - x[0] ** 2) - x[1]])


def dispersion(x):
    return np.array([0.,
                     x[0]])


# Times
T = 10000
dt = 0.001
ts = np.linspace(dt, dt * T, T)

# Brownian motion increments
dws = math.sqrt(dt) * np.random.randn(T)

# Initial value
x0 = np.array([-3, 0.])

# Simulate using Euler--Maruyama
xs_euler_maruyama = np.zeros((T, 2))
x = x0.copy()
for i in range(T):
    x += drift(x) * dt + dispersion(x) * dws[i]
    xs_euler_maruyama[i] = x

# Plot
plt.rcParams.update({
    'text.usetex': True,
    'font.family': "serif",
    'text.latex.preamble': r'\usepackage{amsmath,amsfonts}',
    'font.serif': ["Computer Modern Roman"],
    'font.size': 16})

plt.plot(xs_euler_maruyama[:, 0], xs_euler_maruyama[:, 1], c='black')
plt.scatter(*x0, s=20, c='red', edgecolors=None)
plt.grid(linestyle='--', alpha=0.3, which='both')
plt.xlabel('$X_1(t)$')
plt.ylabel('$X_2(t)$')

plt.tight_layout(pad=0.1)
plt.show()
