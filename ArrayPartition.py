nums = [1,4,3,2]
# nums = [6,2,6,5,1,2]
nums.sort()
n=len(nums)
ans=0
for i in range(0,n,2):
    ans+=nums[i]
print(ans)    
