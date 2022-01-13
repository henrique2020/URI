alignment = 3 #Valor padrão da questão
while True:
    tam = int(input())
    if tam == 0:
        break
    
    tam+=1
    tam = int(tam/2)
    for x in range(-tam+1, tam, 1):
        line = ''
        for y in range(-tam+1, tam, 1):
            if x<=y and x < 0:
                line+=str(abs(x)).rjust(alignment)+' '
            elif x<=y and x >= 0:
                line+=str(abs(y)).rjust(alignment)+' '
            elif x>=y and y < 0:
                line+=str(abs(y)).rjust(alignment)+' '
            else:
                line+=str(abs(x)).rjust(alignment)+' '
        print(line[:-1])
