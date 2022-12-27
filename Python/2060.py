m2 = 0
m3 = 0
m4 = 0
m5 = 0

input()
n = list(map(int, input().split()))
for x in n:
    if x%2 == 0:
        m2 += 1
        if x%4== 0:
            m4 += 1
    if x%3 == 0: m3 += 1
    if x%5 == 0: m5 += 1

print('%d Multiplo(s) de 2' % m2)
print('%d Multiplo(s) de 3' % m3)
print('%d Multiplo(s) de 4' % m4)
print('%d Multiplo(s) de 5' % m5)
