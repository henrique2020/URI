while True:
    try: alunos = int(input())
    except: break

    ordenador = {}
    for _ in range(alunos):
        nome, regiao, distancia = input().split()
        distancia = int(distancia)
        
        if(distancia not in ordenador.keys()): ordenador[distancia] = {}
        if(regiao not in ordenador[distancia].keys()): ordenador[distancia][regiao] = []
        
        ordenador[distancia][regiao].append(nome)
        

    for d in sorted(ordenador.keys()):
        for r in sorted(ordenador[d].keys()):
            for n in sorted(ordenador[d][r]):
                print(n)
