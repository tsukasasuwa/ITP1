
# coding: utf-8

# In[5]:


x=0
y=[]

while True:
    
    y.clear()
    x=input()
    if x=="_":
        break
    for i in range(len(x)):
        y.append(x[i])
    m=int(input())
    for i in range(m):
        h=int(input())
        for j in range(h):
            t=y.pop(0)
            y.append(t)
    for i in y:
        print(i,end="")
    print("")

