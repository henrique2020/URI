for x in range(int(input())):
    n1, l, n2 = input()
    n1 = int(n1)
    n2 = int(n2)
    if n1 == n2:
        print(n1*n2)
    else:
        if l.isupper():
            print(n2-n1)
        else:
            print(n2+n1)
