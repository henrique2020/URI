entradas = int(input())
nomes = []
comportamento = {'+': 0, '-': 0}
for _ in range(entradas):
    d1, d2 = input().split()
    comportamento[d1] += 1
    nomes.append(d2)

nomes.sort()
[print(nome) for nome in nomes]
print('Se comportaram: {} | Nao se comportaram: {}'.format(comportamento['+'], comportamento['-']))
