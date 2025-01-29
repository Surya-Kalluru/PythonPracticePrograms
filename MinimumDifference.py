nums = [9,4,1,7]
# nums = [90]
nums.sort()
n=len(nums)
ans=float("inf")
for i in range(n):
    for j in range(i,n):
        temp=[]
        for m in range(i,j+1):
            temp.append(nums[m])
        if len(temp)==2:
            first=temp[0]
            last=temp[-1] 
            ans=min(ans,last-first)     
print(ans)    

#OPTIMAL SOLUTION

nums = [9,4,1,7]
nums.sort()
n=len(nums)
l=0
k=2
ans=float("inf")
for r in range(n):
    if r-l==k:
        l+=1
    if r-l+1==k:    
        ans=min(ans,nums[r]-nums[l])
print(ans)                   
