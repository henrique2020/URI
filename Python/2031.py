for _ in range(int(input())):
    j1 = input()
    j2 = input()
    
    if j1 == j2:
        if j1 == 'ataque': print('Aniquilacao mutua')
        elif j1 == 'pedra': print('Sem ganhador')
        else: print('Ambos venceram')
    else:
        if(j1 == 'ataque' or j2 == 'papel'): print('Jogador 1 venceu')
        else: print('Jogador 2 venceu')
