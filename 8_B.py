
# coding: utf-8

# In[6]:


while True:
    
    x=int(input())
    if x==0:
        break
    a=int(x/100)
    b=int(x%100/10)
    c=int(x-int(x/10)*10)
    print(a+b+c)

