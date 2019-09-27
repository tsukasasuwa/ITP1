
# coding: utf-8

# In[4]:


count=0
num=int(input())
x=list(map(int,input().split()))
for i in range(num-1):
    y=list(map(int,input().split()))

    if x[0]==y[1]:
        y[0],y[1],y[4],y[5]=y[1],y[5],y[0],y[4]     
    elif x[0]==y[2]:
        y[0],y[2],y[3],y[5]=y[2],y[5],y[0],y[3]
    elif x[0]==y[3]:
        y[0],y[2],y[3],y[5]=y[3],y[0],y[5],y[2] 
    elif x[0]==y[4]:
        y[0],y[1],y[4],y[5]=y[4],y[0],y[5],y[1]     
    elif x[0]==y[5]:
        y[0],y[1],y[4],y[5]=y[5],y[4],y[1],y[0]

    for i in range(4):
        if x[1]==y[1]:
            break
        x[1],x[3],x[4],x[2]=x[3],x[4],x[2],x[1]

    if x==y:
        count=count+1

if count==0:
    print("Yes")
else:
    print("No")

