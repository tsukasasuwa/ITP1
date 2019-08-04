
# coding: utf-8

# In[4]:


for i in range(3000):
    x,y=(int(x) for x in input().split())
    if x==0 and y==0:
        break
    if x<y:
        print(x,end="")
        print(" ",end="")
        print(y)
    elif y<x:
        print(y,end="")
        print(" ",end="")
        print(x)

