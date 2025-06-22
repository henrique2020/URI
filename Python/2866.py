for _ in range(int(input())):
    segredo = input()
    
    decodificado = ''
    for l in segredo[::-1]:
        if(l.islower()): decodificado += l
    
    print(decodificado)