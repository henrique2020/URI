duracao_nota = {'W': 1, 'H': 1/2, 'Q': 1/4,
                'E': 1/8, 'S': 1/16, 'T': 1/32, 
                'X': 1/64}
while True:
    composicao = input()
    if composicao == '*': break
    
    compassos = composicao.split('/')
    
    compassos_corretos = 0
    for compasso in compassos:
        duracao = 0
        for nota in compasso: 
            duracao += duracao_nota[nota]
            
        if duracao == 1: 
            compassos_corretos += 1
    
    print(compassos_corretos)
