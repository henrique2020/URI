while True:
    comandos = int(input())    
    if comandos == 0:
        break

    sequencia = list(input())
    direcao = 'N'
    for comando in sequencia:
        if comando == 'E': 
            if direcao == 'N': direcao = 'O'
            elif direcao == 'O': direcao = 'S'
            elif direcao == 'S': direcao = 'L'
            else: direcao = 'N'
        else:
            if direcao == 'N': direcao = 'L'
            elif direcao == 'L': direcao = 'S'
            elif direcao == 'S': direcao = 'O'
            else: direcao = 'N'
    
    print("%s" % direcao)
