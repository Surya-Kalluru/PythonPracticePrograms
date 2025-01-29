cost = [6,5,7,9,2,2]
# cost = [5,5]
cost.sort()
n=len(cost)
ans=0
count=0
for i in range(n-1,-1,-1):
    if count==2:
        count=0
    else:
        ans+=cost[i]
        count+=1    
print(ans)    
