nums = [3,2,1]
diff=-1
for i in range(len(nums)):
   for j in range(1,len(nums)):
      if i<j and nums[i]<nums[j]:
        diff=max(diff,(nums[j]-nums[i])) 
print(diff)  

#OPTIMAL CODE

# nums = [3,2,1]
# low=nums[0]
# diff=-1
# for i in range(1,len(nums)):
#    if low<nums[i]:
#       temp=nums[i]-low
#       diff=max(temp,diff)
#    low=min(low,nums[i])   
# print(diff)   