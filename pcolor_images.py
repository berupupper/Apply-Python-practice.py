#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np


# In[11]:


import matplotlib.pyplot as plt


# Orientations of 2D arrays & images

# In[42]:


z=np.array([[1,2,3],[4,6,5]])


# In[43]:


print('z:\n',z)


# In[44]:


plt.set_cmap('Oranges_r')
plt.pcolor(z)
plt.show()


# ##

# In[60]:




u = np.linspace(-3, 3, 21)
v = np.linspace(-2,2,41)

X,Y = np.meshgrid(u,v)


Z = np.sin(4*np.sqrt(X**2 + Y**2)) 

plt.pcolor(Z)
plt.show()


# In[ ]:




