abas, cliques = map(int, input().split())

for _ in range(cliques):
    op = input()
    if op == "fechou": abas+=1
    elif op == "clicou": abas-=1

print(abas)
