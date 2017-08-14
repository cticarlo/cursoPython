# -*- coding: utf-8 -*-
"""
Created on Sun Aug 2 11:44:31 2017

Exemplo de grafico 3D

@author: carlos
"""

from pylab import figure, show
from numpy import pi, linspace, sin, cos
from mpl_toolkits.mplot3d import Axes3D

theta = linspace(-4*pi, 4*pi, 100)
z = linspace(-2, 2, 100)
r = z**2 + 1
x = r*sin(theta)
y = r*cos(theta)
r = None

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, label='parametric curve')
ax.legend()
show()
