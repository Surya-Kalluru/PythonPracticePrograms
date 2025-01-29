nums = [2,2,1,1,1,2,2]
dict={}
for i in nums:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
n=len(nums)
temp=n//2
ans=0
for i in dict:
    val=dict[i]
    if val > temp:
        ans=i
print(ans)  

#ANOTHER SOLUTION

nums.sort()
temp=len(nums)//2
print(nums[temp])

    
             