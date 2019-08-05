
# coding: utf-8

# In[16]:


count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n=int(input())
ii=0
while ii<n:
    b,f,r,v=(int(x) for x in input().split())           #b棟f階のr番目の部屋にv人が追加で入居した
    count[b-1][f-1][r-1]=v
    ii+=1
    
for i in range(4):
    for j in range(3):
        for k in range(10):
            print(" ",count[i][j][k],end="")
        print("")
    print("#############################")

