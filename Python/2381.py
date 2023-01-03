alunos, vencedor = map(int, input().split())
lista = []
for _ in range(alunos):
    lista.append(input());

lista.sort()
print(lista[vencedor-1])
