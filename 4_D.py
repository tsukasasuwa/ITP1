
# coding: utf-8

# In[34]:


n=int(input())
a=(input().split())
l=[]
for i in range(n):
    l.append(int(a[i]))
    
print(min(l),end="")
print(" ",end="")
print(max(l),end="")
print(" ",end="")
print(sum(l))

