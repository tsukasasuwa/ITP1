
# coding: utf-8

# In[2]:


while True:
    H,W=(int(x) for x in input().split())
    if H==0 and W==0:
        break
    for i in range(H):
        for j in range(W):
            print("#",end="")
        print("")
    print("")

