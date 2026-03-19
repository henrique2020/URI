# Problema: 2108 - Contando Caracters | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]        | Tempo: 0.000s

import sys

linhas = [linha.split() for linha in sys.stdin.read().splitlines()]
del linhas[-1]

maior = None
char = 0

percorrido = []
for linha in linhas:
    sequencia = []
    for palavra in linha:
        c = len(palavra)
        sequencia.append(c)
        
        if c >= char:
            char = c
            maior = palavra
            
    percorrido.append('-'.join(map(str, sequencia)))
    
print('\n'.join(percorrido), end='\n\n')
print(f"The biggest word: {maior}")
