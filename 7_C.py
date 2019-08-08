
# coding: utf-8

# In[21]:


r,c=(int(x) for x in input().split())
l=[[0 for i in range(c)] for j in range(r)]
ssum=0

for i in range(r):
    x=input().split()
    for j in range(c):
        l[i][j]=int(x[j])
        
print("")

for i in range(r):
    gsum=0
    for j in range(c):
        print(l[i][j],"",end="")
        gsum=gsum+l[i][j]
    print(gsum)

for j in range(c):
    rsum=0
    for i in range(r):
        rsum=rsum+l[i][j]
    print(rsum,"",end="")
    ssum=ssum+rsum
print(ssum)

