from itertools import product
s=0
a=list(product("0123456789ABCDEF",repeat=3))
for i in range(len(a)):
    if a[i][0]!=a[i][1] and a[i][1]!=a[i][2] and a[i][0]!=a[i][2] and a[i][0]!="0":
        res=""
        for j in a[i]:
            x=list("02468ACE")
            y=list("13579BDF")
            if j in x:
                res+="ч"
            else:
                res+="н"
        if res == "чнч" or res == "нчн":
            s+=1
print(s)