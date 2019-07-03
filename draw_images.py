#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt


**Orientations of 2D arrays & images**

z=np.array([[1,2,3],[4,6,5]])
print('z:\n',z)

plt.set_cmap('Oranges_r')
plt.pcolor(z)
plt.show()

#

u = np.linspace(-3, 3, 21)
v = np.linspace(-2,2,41)

X,Y = np.meshgrid(u,v)

Z = np.sin(4*np.sqrt(X**2 + Y**2)) 

plt.pcolor(Z)
plt.show()


**contour line**

plt.contour(X,Y,Z,20,cmap='autumn')


**bivarite distribution**

x=np.array([1,3,5,7,5,3,6,8,4,2,8])
y=np.array([2,4,6,8,83,25,2,5,47,3,7])

plt.hist2d(x,y,bins=(20,20),cmap='ocean')

plt.hexbin(x,y,gridsize=(10,10),cmap='PuBu')

