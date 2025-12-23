# Problema: 3093 - Truco da Galera 1.0 | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]         | Tempo: 0.002s


for _ in range(int(input())):
    sobras = input()
    if('A' in sobras and 'J' in sobras
        and 'Q' in sobras and 'K' in sobras):
        print('Aaah muleke')
    else:
        print('Ooo raca viu')
