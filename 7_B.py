
# coding: utf-8

# In[5]:


while True:
    sum=0
    n,x=(int(x) for x in input().split())   #1 から n までの中から、重複無しで３つの数を選びそれの合計が xとなる組み合わせの数を求める
    if n==0 and x==0:
        break
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i+j+k==x and i!=j and i!=k and j!=k:
                    sum=sum+1
    print(int(sum/6))

