r=10
for i in range(r):
    for j in range(r-i-1):
        print("*",end="")
    for j in range(1):
        print(r-i,end="")   
    print()    