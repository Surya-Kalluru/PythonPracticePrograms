arr = [2,2,2,2,5,5,5,8]
n=len(arr)
ans=0
arr1=[]
k=3
t=4
for i in range(n):
    for j in range(i,n):
        temp=[]
        tsum=0
        for m in range(i,j+1):
            temp.append(arr[m])
            tsum+=arr[m]
        if len(temp)==k:  
            avg=tsum/k
            if avg>=t:
                ans+=1
print(ans)

# OPTIMAL SOLUTION

arr = [2,2,2,2,5,5,5,8]
n=len(arr)
l=0
ans=0
k=3
t=4
for r in range(n):
    temp+=arr[r]
    if (r-l==k):
        temp-=arr[l]
        l+=1
    if (r-l+1==k):
        print(l,r,temp)     
        