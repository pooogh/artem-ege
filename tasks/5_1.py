# print(int('1110', 2))
def to_tri(n):
    itog = ''
    while n != 0:
        itog += str(n % 3)
        n //= 3
    return itog[::-1]
print(to_tri(9)) #100
# 1000 
# len = 4
# 3 -> 10

for n in range(9, 1000):
    tri = to_tri(n) # строка
    if n % 3 != 0:
        tri = '1' + tri + tri[-3] + tri[-2] + tri[-1]
    else:
        sum = 0
        for i in tri:
            sum += int(i)
        dop = to_tri(sum * 8)
        tri = tri + dop
    r = int(tri, 3)
    if 1200 <= r <= 1240:
        print(r)
