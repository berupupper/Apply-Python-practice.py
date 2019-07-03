#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt

doge = plt.imread('doge.jpg')
plt.imshow(doge)   #doge source:https://www.google.com/search?q=doge&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjl4KqLl5njAhWC1lkKHS8kByMQ_AUIECgB&biw=1349&bih=653#imgrc=UWBEFPaDlht07M:
print(doge.shape)

doge_2d = doge.sum(axis=2)
print(doge_2d.shape)


# # Colorful doges!!


plt.imshow(doge_2d,cmap='ocean')
plt.imshow(doge_2d,cmap='autumn')
plt.imshow(doge_2d,cmap='PuBu')
plt.imshow(doge_2d,cmap='gray')
plt.imshow(doge_2d,cmap='plasma')


# # Extent and aspect


plt.imshow(doge_2d,extent=(-1,1,-1,1), aspect=0.5)
plt.imshow(doge_2d,extent=(-1,1,-1,1), aspect=2)
plt.imshow(doge_2d,extent=(-2,2,-1,1), aspect=2)
plt.imshow(doge_2d,extent=(-10,10,-10,10), aspect=1)





plt.subplot(2,2,1)
plt.title('-1,1,-1,1/0.5')
plt.imshow(doge_2d,extent=(-1,1,-1,1), aspect=0.5)

plt.subplot(2,2,2)
plt.title('-1,1,-1,1/2')
plt.imshow(doge_2d,extent=(-1,1,-1,1), aspect=2)

plt.subplot(2,2,3)
plt.title('-2,2,-1,1/2')
plt.imshow(doge_2d,extent=(-2,2,-1,1), aspect=2)

plt.subplot(2,2,4)
plt.title('-10,10,-10,10/1')
plt.imshow(doge_2d,extent=(-10,10,-10,10), aspect=1)

