
# coding: utf-8

# In[3]:


a,b,c=(int(x) for x in input().split())
sum=0
for i in range(a,b):
    if c%i==0:
        sum+=1
print(sum)

