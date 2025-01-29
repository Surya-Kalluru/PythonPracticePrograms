li=[5,9,1,8,7]
n=len(li)
l=0
temp=0
k=3
ans=0
for r in range(n): 
    temp+=li[r]
    if(r-l==k):
       temp-=li[l]
       l+=1
    if(r-l+1==k): 
       ans=max(ans,temp)
print(ans)

















# n=len(li)
# ans=0
# for i in range(n):
#     for j in range(i,n):
#        temp=[]
#        sum=0
#        for k in range(i,j+1):
#            temp.append(li[k])
#            sum+=li[k]
#        if len(temp)==3:
#         ans=max(sum,ans)
# print(ans)