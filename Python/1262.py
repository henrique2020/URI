while True:
    try: 
        processos = input().upper()
        processos_simultaneos = int(input())
    except: break
    
    ciclos = 0
    sequencia = ''
    for processo in processos:
        if processo == 'R':
            sequencia += processo
            if len(sequencia) == processos_simultaneos:
                ciclos += 1
                sequencia = ''
                
        elif processo == 'W':
            ciclos += 1
            if len(sequencia) != 0:
                sequencia = ''
                ciclos += 1
                
    if sequencia: ciclos += 1
    
    print(ciclos)
