# Problema: 3174 - Grupo de Trabalho do Noel | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]               | Tempo: 0.000s

d = { 
    'arquitetos': {'r': 4, 't': 0},
    'bonecos': {'r': 8, 't': 0}, 
    'desenhistas': {'r': 12, 't': 0}, 
    'musicos': {'r': 6, 't': 0}
}

for _ in range(int(input())):
    _, grupo, horas = input().split()
    d[grupo]['t'] += int(horas)

brinquedos = [g['t']//g['r'] for g in d.values()]
print(sum(brinquedos))
