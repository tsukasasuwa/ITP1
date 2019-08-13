
# coding: utf-8

# In[3]:


str=input()
q=int(input())

for i in range(q):
    x=input().split()
    
    if x[0]=="print":
        for i in range(int(x[2])-int(x[1])+1):
            print(str[i+int(x[1])],end="")
        print("")
            
    elif x[0]=="reverse":
        y=[]
        length=len(str)
        
        for i in range(int(x[1])):
            y.append(str[i])
        for i in range(int(x[2])-int(x[1])+1):
            y.append(str[int(x[2])-i])
        for i in range(len(str)-int(x[2])-1):
            y.append(str[i+int(x[2])+1])   
        str=""
        for i in range(length):
            str=str+y[i]
        
    elif x[0]=="replace":
        y=[]
        length=len(str)
        
        for i in range(int(x[1])):
            y.append(str[i])
        for i in range(len(x[3])):
            y.append(x[3][i])
        for i in range(len(str)-int(x[2])-1):
            y.append(str[i+int(x[2])+1])   
        str=""
        for i in range(length):
            str=str+y[i]

