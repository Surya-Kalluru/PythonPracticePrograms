r=5
c=r-1
for i in range(r):
    for j in range(c-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")    
    print()    