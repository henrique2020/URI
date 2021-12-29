pontos = list(map(int, input().split()))
pontos.sort()
if(pontos[1]%pontos[0] == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
