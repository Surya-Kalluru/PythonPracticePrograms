r=5
for i in range(r-1):
    for j in range(r-i):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
          print("*",end="")
        else:
          print(" ",end="")        
    print() 
for i in range(r-1,-1,-1):
    for j in range(r-i):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
          print("*",end="")
        else:
          print(" ",end="")  
    print()  