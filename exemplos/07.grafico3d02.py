# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 11:44:31 2017

Grafico 3D de superficie

@author: carlos
"""

from numpy import pi, sin, cos, linspace,\
                  repeat, append, newaxis
from pylab import figure, show, cm
from mpl_toolkits.mplot3d import Axes3D

nAng = 36
nRad = 8
rad = linspace(0.125, 1.0, nRad)
ang = linspace(0, 2*pi, nAng)
ang = repeat(ang[...,newaxis], nRad, axis=1)

x = append(0, (rad*cos(ang)).flatten())
y = append(0, (rad*sin(ang)).flatten())
z = sin(-x*y)

fig = figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)
show()
