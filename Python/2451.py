# Problema: 2451 - PacMan      | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.000s

pontos = atual = 0
mapa = ''
for n in range(int(input())):
    linha = input()
    mapa += linha if n%2 == 0 else linha[::-1]

for p in mapa:
    if p == 'o': atual += 1
    elif p == 'A':
        if pontos < atual: pontos = atual
        atual = 0

if pontos < atual: pontos = atual
print(pontos)
