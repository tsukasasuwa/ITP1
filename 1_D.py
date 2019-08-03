
# coding: utf-8

# In[6]:


x=input()
x=int(x)
h=int(x/3600)
m=int(x%3600/60)
s=int(x%60)
print(h,end="")
print(":",end="")
print(m,end="")
print(" ",end="")
print(s,end="")

