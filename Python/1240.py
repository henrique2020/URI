for x in range(int(input())):
    n1, n2 = input().split()
    if n1[-len(n2):] == n2:
        print('encaixa')
    else:
        print('nao encaixa')