# nums = [1,2,3,1,1,3]
nums=[1,2,3]
# nums = [1,1,1,1]
temp=0
for i in range(len(nums)):
    for j in range(len(nums)):
       if nums[i]==nums[j] and i<j:
        print(nums[i],nums[j])
        temp+=1
print(temp)            

#OPTMAL SOLUTION

dict={}
for i in nums:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict) 
ans=0
for i in dict:
   n=dict[i]
   temp=n*(n-1)/2
   ans=ans+temp
print(int(ans))   










# n=len(nums)
# temp=0
# val=0
# for i in range(n):
#     for j in range(1,n):
#        if nums[i]==nums[j] and i<j:
#            temp+=1
#            val=max(val,temp)
#        else:
#            val==0    
# print(val)