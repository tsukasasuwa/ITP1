
# coding: utf-8

# In[8]:


x=int(input())
t=0
h=0
for i in range(x):
    taro,hanako=input().split()
    if taro>hanako:
        t=t+3
    elif hanako>taro:
        h=h+3
    elif hanako==taro:
        t=t+1
        h=h+1
print(t, h)

