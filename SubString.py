s="surya"
n=len(s)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=""
        for k in range(i,j+1):
            temp+=s[k]
        ans.append(temp)
print(ans)          