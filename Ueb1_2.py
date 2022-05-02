#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:36:19 2020

@author: csmk
"""

import numpy as np
from math import pi
import matplotlib.pyplot as plt
# a) x(x) = cos(2pi f t) mittels komplexer E-Funktionen

# x(t) = e^(j 2pi ft)  

# b) x(t) = Xe^j2pift

# c)
# t(s) values mit Abtastperiod from 0 -> 1.50 
Abtastperiod=3/20
t_s = np.arange(0,1.60,Abtastperiod)
res = []
def roundedCos(v):
    return round(np.cos(v))

def roundedSin(v):
    return round(np.sin(v))
    
X = 1
periodedauer=1.50

f = 1/periodedauer

x = X*np.cos(2*pi*f*t_s)

for t in t_s:
    real = X*roundedCos(2*pi*f*t)
    imag = X*roundedSin(2*pi*f*t)
    res.append(complex(real,imag))

i=1
for c in res:
    print('['+str(i)+'] : R(x(t)) := ',c.real,' I(x(t)) := ',c.imag,'\n')
    i+=1

plt.subplot(2,1,1)
plt.plot(t_s,x) ; plt.title('Sinusoidal Signal');
plt.xlabel('Time(s)') ; plt.ylabel('Amplitude')    
