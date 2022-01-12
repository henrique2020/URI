while True:
    valores = list(map(str, input().split()))
    if int(valores[0]) == 0 and int(valores[1]) == 0:
        break

    if len(valores[0]) > len(valores[1]): tamanho = len(valores[0])
    else: tamanho = len(valores[1])
    
    c1 = valores[0].zfill(tamanho)
    c2 = valores[1].zfill(tamanho)
    
    
    calc = 0
    sobra = 0
    for x in range(tamanho-1, -1, -1):
        if int(c1[x])+int(c2[x])+sobra >= 10:
            calc += 1
            sobra = 1
        else:
            sobra = 0
    
    if calc == 0: print('No carry operation.')
    elif calc == 1:  print(f'{calc} carry operation.')
    else: print(f'{calc} carry operations.')
