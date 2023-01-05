while (int(input()) != 0):
    suspeitos = list(map(int, input().split()))
    suspeitos_ord = sorted(suspeitos)
    print(suspeitos.index(suspeitos_ord[len(suspeitos)-2])+1)
