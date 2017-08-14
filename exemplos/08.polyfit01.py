# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 23:07:51 2017

@author: carlos
"""
from numpy import array, linspace, polyfit, poly1d
from pylab import plot

nivel = array([2,3,4,5,6,7,8,9,10,11,12,13,14],dtype=float)
l1s = array([43,44,44,47,52,58,62,65,71,77,82,86,86],dtype=float)
l1d = array([43,44,44,47,52,56,61,65,71,77,81,86,86],dtype=float)
l2s = array([43,44,44,47,52,58,62,65,72,77,82,86,86],dtype=float)
l2d = array([43,44,44,46,52,56,61,65,71,77,81,86,86],dtype=float)
l3s = array([43,43,44,47,52,58,62,65,71,77,82,86,86],dtype=float)
l3d = array([43,44,44,46,52,56,61,65,71,75,81,86,86],dtype=float)

lsMed = (l1s+l2s+l3s)/3
ldMed = (l1d+l2d+l3d)/3

plot(nivel, lsMed,'bo')
plot(nivel, ldMed,'ro')

coefS = polyfit(nivel, lsMed, 3)
coefD = polyfit(nivel, ldMed, 3)

curvaS = poly1d(coefS)
curvaD = poly1d(coefD)

x=linspace(nivel[0],nivel[-1],101)

yS = curvaS(x)
yD = curvaD(x)

plot(x, yS,'b')
plot(x, yD,'r')
