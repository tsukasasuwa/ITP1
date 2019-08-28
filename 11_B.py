
# coding: utf-8

# In[5]:


x = list(map(int, input().split()))
num = int(input())
for i in range(num):
    q = list(map(int, input().split()))
    if q[0]==x[0]:
        
        if q[1]==x[1]:
            print(x[2])
        elif q[1]==x[2]:
            print(x[4])
        elif q[1]==x[4]:
            print(x[3])
        elif q[1]==x[3]:
            print(x[1])
            
    elif q[0]==x[1]:
        if q[1]==x[0]:
            print(x[3])
        elif q[1]==x[3]:
            print(x[5])
        elif q[1]==x[5]:
            print(x[2])
        elif q[1]==x[2]:
            print(x[0])
            
    elif q[0]==x[2]:
        if q[1]==x[0]:
            print(x[1])
        elif q[1]==x[1]:
            print(x[5])
        elif q[1]==x[5]:
            print(x[4])
        elif q[1]==x[4]:
            print(x[0])
            
    elif q[0]==x[3]:
        if q[1]==x[0]:
            print(x[4])
        elif q[1]==x[4]:
            print(x[5])
        elif q[1]==x[5]:
            print(x[1])
        elif q[1]==x[1]:
            print(x[0])
            
    elif q[0]==x[4]:
        if q[1]==x[0]:
            print(x[2])
        elif q[1]==x[2]:
            print(x[5])
        elif q[1]==x[5]:
            print(x[3])
        elif q[1]==x[3]:
            print(x[0])
            
    elif q[0]==x[5]:
        if q[1]==x[1]:
            print(x[3])
        elif q[1]==x[3]:
            print(x[4])
        elif q[1]==x[4]:
            print(x[2])
        elif q[1]==x[2]:
            print(x[1])
    

