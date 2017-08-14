# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:44:31 2016

Calcular os senos e cossenos de 360 graus, grau a grau

@author: carlos
"""

from numpy import sin, cos, radians, arange

from pylab import *

ang = arange (0.0, 361.0)
seno    = sin(radians(ang))
cosseno = cos(radians(ang))

plot (ang, seno)
plot (ang, cosseno)
