r=5
for i in range(r):
    for j in range(r-i):
        print(" ",end="")
    for j in range(i+1,0,-1):
        print(j,end="")    
    print()    