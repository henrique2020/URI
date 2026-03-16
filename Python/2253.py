# Problema: 2253 - Validador de Senhas | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]         | Tempo: 0.000s

import sys

def senhaValida():
    print("Senha valida.")

def senhaInvalida():
    print("Senha invalida.")

data = sys.stdin.read().splitlines()
for senha in data:
    if not 6 <= len(senha) <= 32:
        senhaInvalida()
        continue

    if not all(ch.isalnum() for ch in senha):
        senhaInvalida()
        continue

    maiscula = any(ch.isupper() for ch in senha)
    minuscula = any(ch.islower() for ch in senha)
    numero = any(ch.isdigit() for ch in senha)
    
    if maiscula and minuscula and numero:
        senhaValida()
    else:
        senhaInvalida()