for _ in range(int(input())):
    alunos, numero =  map(int, input().split())
    palpites = list(map(int, input().split()))
    
    if numero in palpites: print(palpites.index(numero)+1)
    else:
        chute_mais_proximo = palpites[0]
        for chute in palpites[1:]:
            if abs(numero-chute) < abs(numero-chute_mais_proximo):
                chute_mais_proximo = chute
        print(palpites.index(chute_mais_proximo)+1)
