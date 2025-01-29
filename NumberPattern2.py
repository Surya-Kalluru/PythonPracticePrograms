r=7
for i in range(r):
    for j in range(r-i):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print(k,end="") 
    for z in range(i):
        print(z+2,end="")    
    print()       