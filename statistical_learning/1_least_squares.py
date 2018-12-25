#!/usr/bin/env python3
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

def real_func(x):
    return np.sin(2 * np.pi * x)

def fit_func(p, x):
    f = np.poly1d(p)
    return f(x)

def residuals_func(p, x, y):
    ret = fit_func(p, x) - y
    return ret

x_points = np.linspace(0, 1, 1000)

x = np.linspace(0, 1, 10)
y = [real_func(_x) + np.random.normal(0, 0.1) for _x in x]

def fitting(M=0):
    plt.clf()
    p_init = np.random.rand(M + 1)
    p_lsq = leastsq(residuals_func, p_init, args=(x, y))
    plt.plot(x_points, real_func(x_points), label='real')
    plt.plot(x_points, fit_func(p_lsq[0], x_points), label='fitted curve')
    plt.plot(x, y, 'bo', label='noise')
    plt.legend()
    plt.savefig('1_%d.png' % M)
    return p_lsq

p_lsq_0 = fitting(M=0)
p_lsq_1 = fitting(M=1)
p_lsq_3 = fitting(M=3)
p_lsq_9 = fitting(M=9)
