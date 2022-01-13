while True:
    n = int(input())
    if n == 0:
        break
    
    lista = [1]
    for x in range(1, n*2-1):
        lista.append(lista[x-1]*2)
    alignment = len(str(lista[-1]))
    for x in range(0, n):
        justified = ''
        for y in range(x, x+n):
            justified+=str(lista[y]).rjust(alignment)+' '
        print(justified[:-1])
    print()
