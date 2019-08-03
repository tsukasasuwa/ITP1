
# coding: utf-8

# In[3]:


a,b=(int(x) for x in input().split())
if a<b:
    print("a<b")
elif a>b:
    print("a>b")
elif a==b:
    print("a==b")

