rep = int(input())
for x in range(rep):
    l = list(map(int, input().split()))
    n_reguas = l[0]
    tomadas = sum(l[1:])
    tomadas_livres = tomadas-(n_reguas-1)
    print(tomadas_livres)