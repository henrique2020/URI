alignment = 3 #Valor padrão da questão
while True:
    tam = int(input())
    if tam == 0:
        break
    
    arr = []
    for x in range(tam):
        arr_2 = []
        [arr_2.append(x) for _ in range(tam)]
        arr.append(arr_2)
    print(arr)
    """
    p = 1
    for x in range(tam):
        line = ''
        for y in range(tam):
            #print(x, y, '(', x+y, ')', sep='', end=' ')
            if x+y >= tam:
                line+=(str(p)+'p').rjust(alignment)+' '
            elif x <= y:
                line+=(str(p+x)+'x').rjust(alignment)+' '
            else:
                line+=(str(p+y)+'y').rjust(alignment)+' '
            '''
            if x<=y and x < 0:
                line+=str(abs(x)).rjust(alignment)+' '
            elif x<=y and x >= 0:
                line+=str(abs(y)).rjust(alignment)+' '
            elif x>=y and y < 0:
                line+=str(abs(y)).rjust(alignment)+' '
            else:
                line+=str(abs(x)).rjust(alignment)+' '
            '''
        #print()
        print(line[:-1])
"""
