r=5
for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i or i==r-1:
            print("*",end="")
        else:    
            print(" ",end="")   
    print()    