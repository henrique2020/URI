alternativas = ['A', 'B', 'C', 'D', 'E']
while True:
    rep = int(input())
    if rep == 0: break
    
    for x in range(rep):
        marcacoes = list(map(int, input().split()))
        resposta = ''
        count_marcacoes = 0
        for m in range(len(marcacoes)):
            if marcacoes[m] <= 127:
                resposta = alternativas[m]
                count_marcacoes += 1
        if count_marcacoes != 1:
            resposta = '*'
        print(resposta)