li=[2,6,1,5,0]
n=len(li)
for i in range(0,n-1):
    isSwapped=False
    for j in range(0,n-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            isSwapped=True
    if(isSwapped==False):
       break       
    print(li)            