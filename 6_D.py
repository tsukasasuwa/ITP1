
# coding: utf-8

# In[15]:


n,m=(int(x) for x in input().split())
A = [[0 for i in range(m)] for j in range(n)]
B = []
b=0

for i in range(n):
    l=input().split()
    for j in range(m):
        A[i][j]=int(l[j])
        
for i in range(m):
    b=int(input())
    B.append(b)

print("")
for i in range(n):
    ans=0
    for j in range(m):
        ans=ans+A[i][j]*B[j]
    print(ans)   

