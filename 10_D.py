
# coding: utf-8

# In[2]:


import math
import numpy as np
n=int(input())
x=input().split()
y=input().split()
p1=0
p2=0
p3=0
pi=[]
for i in range(n):
    p1=p1+abs(float(x[i])-float(y[i]))
    p2=p2+(float(x[i])-float(y[i]))**2
    p3=p3+(float(x[i])-float(y[i]))**3
    pi.append(float(x[i])-float(y[i]))
print(p1)
print(math.sqrt(p2))
print(np.power(p3,1/3))
print(max(pi))

