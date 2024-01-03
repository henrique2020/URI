while True:
    n_cartas = int(input())
    if n_cartas == 0: break
    
    cartas = [n+1 for n in range(n_cartas)]
    removidas = []
    
    while(len(cartas) > 1):
        removidas.append(cartas[0])
        del cartas[0]
        if len(cartas) > 0:
            cartas.append(cartas[0])
            del cartas[0]
            
    print("Discarded cards: {}".format(', '.join(str(x) for x in removidas)))
    print("Remaining card: {}".format(str(cartas[0])))
