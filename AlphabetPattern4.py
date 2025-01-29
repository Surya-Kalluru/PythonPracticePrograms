r=5
for i in range(r-1,-1,-1):
    for j in range(r-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(65+j),end=" ")    
    print()    