list=[1,5,1,4,1,5,4]
n=len(list)
dict={}
for i in range(n):
    temp=list[i]
    if temp not in dict:
        dict[temp]=1
    else:
        dict[temp]=dict[temp]+1
print(dict) 

#ANOTHER CODE

list=[1,5,1,4,1,5,4]
n=len(list)
dict={}
for i in list:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
print(dict)            



