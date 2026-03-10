# Problema: 3141 - Dúvida Etária | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]   | Tempo: 0.356s

from datetime import date

def pegaData():
    entrada = list(map(int, input().split('/')))
    return entrada[::-1]

nome = input()
dt_atual = date(*pegaData())
dt_nascimento = date(*pegaData())

anos = dt_atual.year - dt_nascimento.year
if(dt_atual.month < dt_nascimento.month 
   or (
       dt_atual.month == dt_nascimento.month 
       and dt_atual.day < dt_nascimento.day
    )):
    anos -= 1

if(dt_nascimento.strftime('%m-%d') == dt_atual.strftime('%m-%d')):
    print("Feliz aniversario!")

print(f"Voce tem {anos} anos {nome}.")