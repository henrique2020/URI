def imprime(lista):
    for linha in lista:
        print(''.join(linha))
    print('@')

while True:
    tamanho = int(input())
    if tamanho == 0:
        break
    
    lista = [['O' for _ in range(tamanho)] for _ in range(tamanho)]
    
    x = y = int(tamanho/2)
    lista[x][y] = 'X'
    
    imprime(lista)

    espiral = {'D': 1, 'C': 1, 'E': 2, 'B': 2}
    fim = False
    while not fim:
        if x == y and x == tamanho-1:
            break
        
        for d, m in espiral.items():
            for _ in range(m):                
                lista[x][y] = 'O'
                if(d == 'D'): y+=1
                elif(d == 'E'):y-=1
                elif(d == 'C'): x-=1
                elif(d == 'B'): x+=1
                
                if x == tamanho or y == tamanho:
                    fim = True
                    break
                
                lista[x][y] = 'X'
                imprime(lista)
                
            if fim:
                break
            
            espiral[d] += 2