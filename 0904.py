'''from itertools import product
a = list(product ("АПРСУ", repeat =5))
for i in range(len(a)):
    if a[i].count('А') == 0:
        print(i)
        break'''
from itertools import product
s=0
a = list(product('01234567', repeat=5))
print(a[0])
for i in range(len(a)):
    if a[i].count('6') == 1 and a[i][0]!='0':
        b=a[i].index('6')
        if b+1==5:
            if int(a[i][b-1])%2==0:
                s+=1
            continue
        if b-1 ==0:
            if int(a[i][b+1])%2==0:
                s+=1
            continue
        if int(a[i][b+1])%2==0 and int(a[i][b-1])%2==0 and b+1!=5 and b-1!=0:
            s+=1
print(s)