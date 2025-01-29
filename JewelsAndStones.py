jewels = "aA"
stones = "aAAbbbb"
temp=0
for i in jewels:
    for j in stones:
        if j==i:
            temp+=1
print(temp)   

#OPTIMAL SOLUTION

dict={}
temp=0
for i in stones:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)        
for i in range(len(jewels)):
    ch=jewels[i]
    if ch in dict:
        temp+=dict[ch]
print(temp)

