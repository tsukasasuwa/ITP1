
# coding: utf-8

# In[11]:


import math
x=input()
r=float(x)
a=r*r*math.pi
b=2*r*math.pi
print("{0:.5f}".format(a),end="")
print(" ",end="")
print("{0:.6f}".format(b))

