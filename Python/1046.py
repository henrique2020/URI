hI, hF = input().split()
hI = int(hI)
hF = int(hF)
if hI > hF: duracao = 24 - (hI - hF)
elif hF > hI: duracao = hF - hI
else: duracao = 24

print("O JOGO DUROU %d HORA(S)" %duracao)
