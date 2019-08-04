
# coding: utf-8

# In[2]:


while True:
    H,W=(int(x) for x in input().split())
    if H==0 and W==0:
        break
    for i in range(H):
        for j in range(W):
            if i%2==0:
                if j==0 or j%2==0:
                    print("#",end="")
                else:
                    print(".",end="")
            if i%2==1:
                if j==1 or j%2==1:
                    print("#",end="")
                else:
                    print(".",end="")
        print("")
    print("")

