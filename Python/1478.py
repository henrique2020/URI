alignment = 3 #Valor padrão da questão
while True:
    tam = int(input())
    if tam == 0:
        break
    
    tam+=1
    for x in range(1, tam):
        line = ''
        for y in range(1, tam):
            if x == y:
                #print('1', end='')
                line+=str(1).rjust(alignment)+' '
            else:
                #print('2', end='')
                line+=str(1+abs(x-y)).rjust(alignment)+' '
        print(line[:-1])
    print()
