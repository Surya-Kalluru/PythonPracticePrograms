li=[1,8,9]
n=len(li)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1): 
            temp.append(li[k])
        print(temp)
        ans.append(temp)
print(ans)            