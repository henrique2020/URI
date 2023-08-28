n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1+n3 <= 2*n2:
    print(2*n1 + 2*n3)
elif n1 > n2 and n1 > n3:
    print(2*n2 + 4*n3)
elif n3 > n1 and n3 > n2:
    print(4*n1 + 2*n2)