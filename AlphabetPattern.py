r=5
alpha=65
for i in range(r):
    for j in range(r-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print(chr(alpha),end=" ") 
        alpha+=1 
        if alpha > 90:
            alpha=65  
    print()    