# Problema: 1247 - Guarda Costeira | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]     | Tempo: 0.004s

LIMITE = 12
while True:
    try: d, vf, vg = map(int, input().split())
    except: break
    
    tf = LIMITE / vf
    tg = (d**2 + LIMITE**2) ** 0.5 / vg
    print('S' if tg <= tf else 'N')