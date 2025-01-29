colors=[1,1,1,6,1,1,1]
colors=[1,8,3,8,3]
maxval=3
for i in range(len(colors)):
    for j in range(1,len(colors)):
        # print(j,i)
        if colors[j]!=colors[i]:
          diff=abs(i-j)
          maxval=max(maxval,diff)
print(maxval)

#OPTIMAL CODE

# maxval=0
# for i in range(len(colors)-1,-1,-1):
#     if colors[0]!=colors[i]:
#         temp=i-0
#         maxval=max(temp,maxval)
#         break
# for i in range(len(colors)):
#     if colors[len(colors)-1]!=colors[i]:
#         temp=len(colors)-1-i
#         maxval=max(temp,maxval)
#         break        
# print(maxval) 