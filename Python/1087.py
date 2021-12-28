while True:
    try: pos = list(map(int, input().split()))  #{ Dá um BREAK caso o input }
    except: break                               #{ do 'pos' esteja vazio    }

    if pos[0] == pos[2] and pos[1] == pos[3]:   ## Verifica se já está na posição final
        if 0 in pos: ## Verificação extra, caso alguma das coordenadas passadas (X1, Y1, X2, Y2) seja 0 (fora do tabuleiro)
            break
        print('0')

    elif pos[0] == pos[2] or pos[1] == pos[3]:  ## Verifica se está na mesma linha ou coluna
        print('1')

    elif abs(pos[0]-pos[2]) == abs(pos[1]-pos[3]):  ## Verifica se está na mesma diagonal 
        print('1')
        
    else:   ## Qualquer caso que não se enquadre no resto, a dama nunca andará mais de 2 casa
        print('2')
