# Problema: 1367 - Ajude!      | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.015s

import sys

linhas = sys.stdin.read().splitlines()
i = 0
while (submissoes := int(linhas[i])) != 0:
    i += 1
    tentativas = {}
    tempo = sucessos = 0
    for submissao in linhas[i:i+submissoes]:
        q, t, r = submissao.split()
        if q not in tentativas:
            tentativas[q] = {'sucesso': False, 'falhas': 0}
        
        if r == 'correct': 
            tempo += int(t)
            sucessos += 1
            tentativas[q]['sucesso'] = True
        else: tentativas[q]['falhas'] += 1
            
    tempo += sum(t['falhas'] * 20 for t in tentativas.values() if t['sucesso'])
    print(f"{sucessos} {tempo}")
            
    i += submissoes
