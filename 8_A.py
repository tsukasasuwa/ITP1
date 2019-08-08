
# coding: utf-8

# In[10]:


x=input()
for i in x:
    
    if i.isupper():
        print(i.lower(),end="")
    elif i.islower():
        print(i.upper(),end="")
    else:
        print(i,end="")

