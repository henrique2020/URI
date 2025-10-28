# Problema: 2543 - Jogatina UFPR | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]   | Tempo: 0.187s

while True:
    try: publicacoes, identificador = input().split()
    except: break
    CS = 0
    for _ in range(int(publicacoes)):
        id, jogo = input().split()
        if id == identificador and jogo == '0': 
            CS += 1
    print(CS)
