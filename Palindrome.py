s=input("enter a string:")
st=""
for i in range(len(s)-1,-1,-1):
    st=st+s[i]
print(st)
if st==s:
    print("string is palindrome")
else:
    print("string is not palindrome")    