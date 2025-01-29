r=5
alpha=65
for i in range(r):
    for j in range(i):
        print(" ",end=" ")
    for j in range(2*r-2*i-1):
        print(chr(alpha),end=" ") 
        alpha+=1  
        if alpha > 69:
            alpha=65     
    print()    