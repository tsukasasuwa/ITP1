
# coding: utf-8

# In[2]:


W,H,x,y,r=(int(x) for x in input().split())
if (x>r and x<W-r)and(y>r and y<H-r):
    print("Yes")
else:
    print("No")

