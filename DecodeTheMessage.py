key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
dict={}
msg=""
temp=97
for i in key:
    if i!=" " and i not in dict:
        dict[i]=chr(temp)
        temp+=1
for i in message:
    if i==" ":
      msg+=" "
    else:
      msg+=dict[i]
print(msg)