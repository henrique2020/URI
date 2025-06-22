for _ in range(int(input())):
    linhas, colunas = map(int, input().split())
    print((linhas // 3) * (colunas // 3))