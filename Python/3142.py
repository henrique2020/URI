hile True:
    try: coluna = input()
    except: break

    tamanho = len(coluna)
    if (tamanho == 3 and coluna > 'XFD') or tamanho > 3:
        print('Essa coluna nao existe Tobias!')
    else:
        if tamanho == 1: indice = (ord(coluna[0])-64)*(26**(tamanho-1))
        elif tamanho == 2: indice = (ord(coluna[0])-64)*(26**(tamanho-1)) + (ord(coluna[1])-64)*(26**(tamanho-2))
        else: indice = (ord(coluna[0])-64)*(26**(tamanho-1)) + (ord(coluna[1])-64)*(26**(tamanho-2)) + (ord(coluna[2])-64)*(26**(tamanho-3))
        
        print(indice)
