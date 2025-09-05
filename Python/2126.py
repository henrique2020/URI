# Problema: 2126 - Procurando Subsequências     | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]                  | Tempo: 0.000s

rep = 0
while True:
    try: 
        subsequencia = input()
        sequencia = input()
    except: break
    
    rep += 1
    
    print(f'Caso #{rep}:')
    if subsequencia in sequencia:
        print(f'Qtd.Subsequencias: {sequencia.count(subsequencia)}')
        print(f'Pos: {sequencia.rfind(subsequencia)+1}')   
    else:
         print('Nao existe subsequencia')
    print()