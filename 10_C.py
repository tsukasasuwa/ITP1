
# coding: utf-8

# In[5]:


import math
while True:
    n=int(input())
    if n==0:
        break
    sum=0
    t=[]
    s=input().split()
    for i in range(n):
        sum=sum+float(s[i])
        t.append(float(s[i]))
    m=sum/n
    hhh=0
    for i in range(n):
        hhh=hhh+(float(s[i])-m)**2
    ans=math.sqrt(hhh/n)
    
    print(ans)

