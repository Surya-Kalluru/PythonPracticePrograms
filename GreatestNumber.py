arr = [17,18,5,4,6,1]
arr1=[]
for i in range(len(arr)-1):
   diff=0
   for j in range(i+1,len(arr)):
      diff=max(diff,arr[j])
   arr1.append(diff)
arr1.append(-1)
print(arr1)   

#OPTIMAL CODE

rmax=-1
for i in range(len(arr)-1,-1,-1):
    temp=arr[i]
    arr[i]=rmax
    rmax=max(temp,rmax)
print(arr)