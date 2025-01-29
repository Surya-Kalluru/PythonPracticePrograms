r=5
c=5
for i in range(r):
    for j in range(r-i):
        print(" ",end="")
    for k in range(c):
        print("*",end="")    
    print()    