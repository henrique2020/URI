entradas = int(input())
nomes = {}
for _ in range(entradas):
    nome = input().capitalize()
    inicial = nome[0]

    if inicial not in nomes.keys(): nomes[inicial] = []
    nomes[inicial].append(nome)

for inicial in sorted(nomes.keys()):
    for nome in nomes[inicial]:
        print(nome)
