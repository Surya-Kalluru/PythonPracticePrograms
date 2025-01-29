nums = [1,2,2,4]
duplicate=0
missing=0
s=set()
for i in range(len(nums)):
    val=nums[i]
    if val not in s:
        s.add(val)
    else:
        duplicate=val
for i in range(1,len(nums)+1):
    if i not in s:
        missing=i
print(duplicate,missing)    

     