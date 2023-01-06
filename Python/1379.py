while True:
    numeros = list(map(int, input().split()))
    if sum(numeros) == 0: break
    
    numeros.sort()
    c = 2*numeros[0] - numeros[1]
    print(c)
