# Problema: 1263 - Aliteração  | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.036s

import sys

linhas = sys.stdin.read().splitlines()
for linha in linhas:
    palavras = linha.split()
    inicial = None
    aliteracao = False
    aliteracoes = 0
    
    for palavra in palavras:
        pLetra = palavra[0].lower()
        if inicial != pLetra:
            inicial = pLetra
            aliteracao = False
        elif not aliteracao:
            aliteracao = True
            aliteracoes += 1
            
    print(aliteracoes)
    
