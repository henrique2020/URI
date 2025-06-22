for _ in range(int(input())):
    dieta = set(input())
    cafe = input()
    almoco = input()
    
    consumido = set(cafe + almoco)
    if(consumido - dieta):
        jantar = 'CHEATER'
    else:
        jantar = ''.join(sorted(dieta - consumido))
    
    print(jantar)