while True:
    planetas = int(input())
    if planetas == 0: break
    
    prmeiro = ['', float('inf')]
    for _ in range(planetas):
        planeta, ano_recebido, tempo_decorrido = input().split()
        ano_enviado = int(ano_recebido) - int(tempo_decorrido)
        
        if ano_enviado < prmeiro[1]:
            prmeiro = [planeta, ano_enviado]

    print(prmeiro[0])