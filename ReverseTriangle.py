r=5
c=r-1
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for j in range(2*r-2*i-1):  
        print("*",end="")  
    print()     

#ANOTHER CODE

# r=5
# c=r-1
# for i in range(r-1,-1,-1):
#     for j in range(c-i):
#         print(" ",end="")
#     for j in range(2*i+1):  
#         print("*",end="")  
#     print()     