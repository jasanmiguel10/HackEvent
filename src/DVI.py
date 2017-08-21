# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 01:59:17 2017

@author: Pablo
"""
import numpy as np

E=0
R=0
for i in range(h_1.shape[0]):
    for j in range(h_2.shape[0]):
        x,y=np.abs(np.array(h_1.index[i])-np.array(h_2.index[j]))
        if (np.sqrt(np.square(x)+np.square(y))<0.5):
            R+=1
            break
    E+=1
   
E+R==h_1.shape[0]
print('Variabilidad dinámica: '+str(E/(E+R)))