# Problema: 2062 - OBI URI     | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.000s

import sys

linhas = sys.stdin.read().splitlines()
palavras = linhas[1].split()

substituir = {'OB': 'OBI', 'UR': 'URI'}

palavras = [substituir.get(palavra[:2], palavra) if len(palavra) == 3 else palavra 
            for palavra in palavras]

print(' '.join(palavras))
