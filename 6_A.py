
# coding: utf-8

# In[8]:


n=int(input())
l=input().split()
for i in range(n+1):
    if i!=0:
        print(l[-i],end="")
        print(" ",end="")

