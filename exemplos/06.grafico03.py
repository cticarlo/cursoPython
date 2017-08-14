# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:44:31 2016

Calcular os senos e cossenos de 360 graus, grau a grau

@author: carlos
"""

from numpy import sin, cos, linspace, pi
from pylab import *

ang = linspace (0.0, 2*pi, 361)
seno    = sin(ang)
cosseno = cos(ang)

cla()
plot (ang, cosseno, color='r', linewidth=2,
      label=r'$\cos(\theta)$')
plot (ang, seno, color='b', linewidth=2,
      label='sin(ang)')

ylim (-1.1,1.1)
xlim (0,2*pi)
title(u"Funções trigonométricas", fontsize=24)
xlabel(u"Ângulo(radianos)")
ylabel(u"função(ângulo)")
legend(loc=3)
