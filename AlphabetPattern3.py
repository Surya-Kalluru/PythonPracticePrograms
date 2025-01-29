r=5
for i in range(r):
    for j in range(r-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print(chr(65+j),end=" ") 
    print()    