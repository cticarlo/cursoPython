# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 01:05:40 2017

@author: carlos
"""
from numpy import sin, pi, linspace
from scipy.integrate import odeint
from pylab import plot, legend, xlabel, grid


def pendulo(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*sin(theta)]
    return dydt

b = 0.25 # constantes
c = 5.0  # constantes
t = linspace(0, 10, 1001) # instantes
y0 = [pi-0.1, 0.0] # ponto inicial[pos,vel]    

res = odeint(pendulo, y0, t, args=(b, c))

plot(t, res[:, 0], 'r', label=r'$\theta(t)(rad)$')
plot(t, res[:, 1], 'b', label=r'$\omega(t)(rad/s)$')
legend(loc='best')
xlabel('t')
grid()
