# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:44:31 2016

Calcular os senos e cossenos de 360 graus, grau a grau

@author: carlos
"""

#import math
from math import sin, cos, radians
from pylab import *

ang = range(0,361)
seno = []
cosseno = []

for a in ang:
    seno.append(sin(radians(a)))
    cosseno.append(cos(radians(a)))
    
print seno    

plot (ang, seno)
plot (ang, cosseno)
