
# coding: utf-8

# In[4]:


a,b,c=(int(x) for x in input().split())
if a<b and b<c:
    print("Yes")
else:
    print("No")

