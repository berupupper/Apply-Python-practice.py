#!/usr/bin/env python
# coding: utf-8


import pandas as pd

df1={'month':('jan','feb'),
    'eggs':(10,5.0),
    'salt':(12.0,5),
    'spam':(15,20.0)}

df1 = pd.DataFrame(df1)

df2={'month':('jan','feb'),
    'ham':(5,2.5),
    'pepper':(6,2.5),
    'spam':(7.5,10)}


# In[45]:


df2=pd.DataFrame(df2)

print(df1)
print(df2)


#####1
m_left= pd.merge(df1,df2,how='left')
print(m_left)

#####2
m_right= pd.merge(df1,df2,how='right')
print(m_right)

#####3
m_outer= pd.merge(df1,df2,how='outer')
print(m_outer)

m_outer1= pd.merge(df2,df1,how='outer')  #adjusted the order of df1, df2
print(m_outer1)

#####4
m_inner= pd.merge(df1,df2,how='inner')
print(m_inner)

m_inner= pd.merge(df2,df1,how='inner')
print(m_inner)
# adjusted the order of df1,df2

