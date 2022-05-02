#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:08:24 2019

@author: csmk
"""

import numpy as np
from math import pi,pow
from time import perf_counter


# usefull statements

step=round(pow(10,6))
f = 1/step
x=np.array(1000000)
steps = np.linspace(0,2*pi,step)

# end 

# 1 Mit expliziter for-Schleife
array1 = np.empty(step,tuple)
t1_start = perf_counter()

j=0
for i in np.linspace(0,2*pi,round(pow(10,6))):
    array1[j] = (np.sin(i),np.cos(i),np.exp(i))
    j+=1
t1_stop = perf_counter()
 
print('DAUER',t1_stop-t1_start)

# 2 Mit expliziter for-Schleife result in list
array2 = []
t2_start = perf_counter()
for i in np.linspace(0,2*pi,round(pow(10,6))):
    array2.append((np.sin(i),np.cos(i),np.exp(i)))
t2_stop = perf_counter()
 
print('DAUER',t2_stop-t2_start)

# 3 Ohne expliziter Schleife
t3_start = perf_counter()
array3 = (np.sin(np.linspace(0,2*pi,round(pow(10,6)))),np.cos(np.linspace(0,2*pi,round(pow(10,6)))),np.exp(np.linspace(0,2*pi,round(pow(10,6)))))
t3_stop = perf_counter() 

print('DAUER',t3_stop-t3_start)

#print('array1_Size = ',array1.size,'\narray2_Size = ',step,'\narray3_Size = ',array3)
    


