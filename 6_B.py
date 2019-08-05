
# coding: utf-8

# In[12]:


cards = [[False for i in range(13)] for j in range(4)]
pattern = ["S", "H", "C", "D"]
n=int(input())
ii=0

while ii<n:
    a,b=input().split()
    cards[pattern.index(a)][int(b)-1]=True
    ii+=1
print("")

for i in range(4):
    for j in range(13):
        if cards[i][j] == False:
            print(pattern[i], j+1)

