s = "xyzzaz"
n=len(s)
ans=0
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
           temp.append(s[k])
        if len(temp)==3 and len(set(temp))==3:
            print(temp)        

# OPTIMAL SOLUTION

s = "xyzzaz"
n=len(s)
l=0
ans=0
k=3
dict={}
for r in range(n):
    if s[r] in dict:
        dict[s[r]]+=1
    else:
        dict[s[r]]=1
    if (r-l==k):
        dict[s[l]]-=1
        if dict[s[l]]==0:
            dict.pop(s[l])
        l+=1
    if len(dict)==3: 
        print(dict)
              