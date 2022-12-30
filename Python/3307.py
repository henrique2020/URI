from math import sqrt
pi = 3.14

entradas = int(input())
for _ in range(entradas):
    area = int(input())
    r = sqrt(area / (4*pi))
    
    if(r < 12): print(f'vermelho = R$ {area*0.09:.2f}')
    elif(r <= 15): print(f'azul = R$ {area*0.07:.2f}')
    else: print(f'amarelo = R$ {area*0.05:.2f}')
