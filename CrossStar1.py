r=10
c=5
for i in range(r):
    for j in range(i):
       print(" ",end="")
    for k in range(2*r-2*i-1):
       print("*",end="")
    print()    
