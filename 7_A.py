
# coding: utf-8

# In[1]:


m=0
f=0
r=0

n=0

while True:#m!=-1 and f!=-1 and r!=-1:     #中間試験の点数 m、期末試験の点数 f、再試験の点数 r 
    
    m,f,r=(int(x) for x in input().split())
    
    if (m==-1 and f==-1 and r==-1) or n>49:
        break
    elif m==-1 or f==-1:
        print("F")
    elif m+f>=80:
        print("A")
    elif m+f>=65 and m+f<80:
        print("B")
    elif m+f>=50 and m+f<65:
        print("C")
    elif m+f>=30 and m+f<50:
        if r>=50:
            print("C")
        elif r<50:
            print("D")
    elif m+f<30:
        print("F")
    
    n=n+1

