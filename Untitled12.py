#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def moving_average(a, n=3) :
    x = np.cumsum(a, dtype=float)
    x[n:] = x[n:] - x[:-n]
    return x[n - 1:] / n


# In[2]:


a = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
print(moving_average(a, n=3))


# In[ ]:




