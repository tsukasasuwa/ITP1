
# coding: utf-8

# In[1]:


for i in range(10000):
    a=input()
    x=int(a)
    if x==0:
        break
    print("case",end="")
    print(" ",end="")
    print(i+1,end="")
    print(":",end="")
    print(" ",end="")
    print(x)

