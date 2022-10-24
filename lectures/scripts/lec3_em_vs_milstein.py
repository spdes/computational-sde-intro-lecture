"""
A computational introduction to stochastic differential equations.

Lecture 3.

https://github.com/spdes/computational-sde-intro-lecture.

Euler--Maruyama vs Milstein's method.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(666)

alp = 1.


def drift(x):
    return - alp ** 2 / 2 * x


def dispersion(x):
    return alp * np.sqrt(1 - x ** 2)


def derivative_of_dispersion(x):
    return -alp * x / np.sqrt(1 - x ** 2)


# Times
T = 500
dt = 0.01
ts = np.linspace(dt, dt * T, T)

# Brownian motion increments and the Brownian motion
dws = math.sqrt(dt) * np.random.randn(T)
ws = np.cumsum(dws)

# Initial value
x0 = 0.

# True solution. See Exercise 1, Assignment 2.
xs_true = np.sin(alp * ws)

# Simulate using Euler--Maruyama
xs_euler_maruyama = np.zeros((T,))
x = x0
for i in range(T):
    x += drift(x) * dt + dispersion(x) * dws[i]
    xs_euler_maruyama[i] = x

# Simulate using Milstein's method
xs_milstein = np.zeros((T,))
x = x0
for i in range(T):
    x += drift(x) * dt + dispersion(x) * dws[i] + 0.5 * derivative_of_dispersion(x) * dispersion(x) * (dws[i] ** 2 - dt)
    xs_milstein[i] = x

# Plot
plt.rcParams.update({
    'text.usetex': True,
    'font.family': "serif",
    'text.latex.preamble': r'\usepackage{amsmath,amsfonts}',
    'font.serif': ["Computer Modern Roman"],
    'font.size': 16})

# Plot trajectories
plt.figure()
plt.plot(ts, xs_true, label='Truth')
plt.plot(ts, xs_euler_maruyama, label='Euler--Maruyama')
plt.plot(ts, xs_milstein, label='Milstein')
plt.grid(linestyle='--', alpha=0.3, which='both')
plt.xlabel('$t$')
plt.ylabel('$X(t)$')
plt.legend()

plt.tight_layout(pad=0.1)
plt.show()

# Plot error
plt.figure()
plt.plot(ts, np.abs(xs_euler_maruyama - xs_true), label='Euler--Maruyama error')
plt.plot(ts, np.abs(xs_milstein - xs_true), label='Milstein error')
plt.grid(linestyle='--', alpha=0.3, which='both')
plt.xlabel('$t$')
plt.ylabel('Absolute error')
plt.legend()
plt.yscale('log')

plt.tight_layout(pad=0.1)
plt.show()
