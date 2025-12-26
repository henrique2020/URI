# Problema: 3161 - As Frutas Esquecidas | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]          | Tempo: 0.000s

n, m = map(int, input().split())
frutas = []
for _ in range(n):
    f = input().lower()
    frutas.append({
        'original': f,
        'inverso': f[::-1],
        'gosta': False
    })

for _ in range(m):
    consulta = input().lower()
    for fruta in frutas:
        if fruta['original'] in consulta or fruta['inverso'] in consulta:
            fruta['gosta'] = True

for fruta in frutas:
    if fruta['gosta']: print(f"Sheldon come a fruta {fruta['original']}")
    else: print(f"Sheldon detesta a fruta {fruta['original']}")
