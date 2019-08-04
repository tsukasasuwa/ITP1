
# coding: utf-8

# In[10]:


a,b,=(float(x) for x in input().split())
d=int(a/b)
r=int(a%b)
f=(a/b)
print(d,end="")
print(" ",end="")
print(r,end="")
print(" ",end="")
print("{0:.5f}".format(f))

