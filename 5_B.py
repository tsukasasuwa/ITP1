
# coding: utf-8

# In[1]:


while True:
    H,W=(int(x) for x in input().split())
    if H==0 and W==0:
        break
    for i in range(H):
        if i==0 or i==H-1:
            for z in range(W):
                print("#",end="")
            print("")
        else:
            for j in range(W):
                if j==0 or j==W-1:
                    print("#",end="")
                else:
                    print(".",end="")
            print("")
    print("")

