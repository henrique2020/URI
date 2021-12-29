num = int(input())
for x in range(2, num, 2):
    print('%d^2 = %d' % (x, pow(x, 2)))

if num%2 == 0:
    print('%d^2 = %d' % (num, pow(num, 2)))
