t_saques = 0    #Tentativas de saques
s_saques = 0    #Saques bem sucedidos

t_bloqueios = 0    #Tentativas de bloqueios
s_bloqueios = 0    #Bloqueios bem sucedidos

t_ataques = 0    #Tentativas de ataques
s_ataques = 0    #Ataques bem sucedidos

jogadores = int(input())
for _ in range(jogadores):
    input()
    #Ordem: 0 => Saques, 1 => Bloqueios, 2 => Ataques
    tentativas = list(map(int, input().split()))
    sucessos = list(map(int, input().split()))
    
    t_saques += tentativas[0]
    s_saques += sucessos[0]
    
    t_bloqueios += tentativas[1]
    s_bloqueios += sucessos[1]
    
    t_ataques += tentativas[2]
    s_ataques += sucessos[2]
    
print('Pontos de Saque: {:.2f} %.'.format((s_saques*100)/t_saques))
print('Pontos de Bloqueio: {:.2f} %.'.format((s_bloqueios*100)/t_bloqueios))
print('Pontos de Ataque: {:.2f} %.'.format((s_ataques*100)/t_ataques))
