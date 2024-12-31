jogadas_vencedoras = {
    'tesoura': ['papel', 'lagarto'], 
    'papel': ['pedra', 'spock'], 
    'pedra': ['lagarto', 'tesoura'], 
    'lagarto': ['spock', 'papel'], 
    'spock': ['tesoura', 'pedra']
}
rep = int(input())
for _ in range(rep):
    r, s = input().lower().split()
    
    if r == s: print('empate')
    elif s in jogadas_vencedoras[r]: print('rajesh')
    else: print('sheldon')
