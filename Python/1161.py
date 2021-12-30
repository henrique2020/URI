from math import factorial as fac
while True:
    try: n1, n2 = map(int, input().split())
    except: break

    sum = fac(n1)+fac(n2)
    print(sum)
