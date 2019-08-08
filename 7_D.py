
# coding: utf-8

# In[19]:


n,m,l=(int(x) for x in input().split())
A=[[0 for i in range(m)] for j in range(n)]
B=[[0 for i in range(l)] for j in range(m)]
C=[[0 for i in range(l)] for j in range(n)]

for i in range(n):
    x=input().split()
    for j in range(m):
        A[i][j]=int(x[j])
        
for i in range(m):
    x=input().split()
    for j in range(l):
        B[i][j]=int(x[j])

print("")

for k in range(n):
    for i in range(n):
        c=0
        for j in range(m):
            c=c+A[k][j]*B[j][i]
        print(c,"",end="")
    print("")

