case = 1
while True:
    rep = int(input())
    if rep == 0: break

    j = z = 0
    print(f'Teste {case}')
    for _ in range(rep):
        t = list(map(int, input().split()))
        j += t[0]
        z += t[1]
        print(j-z)
    print()
    case += 1
