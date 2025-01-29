r=5
for i in range(r):
    for j in range(r):
      if i==j or j==r-i-1:
        print("*",end="")   
      else:
        print(" ",end="")    
    print()
