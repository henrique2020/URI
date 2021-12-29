pontos = list(map(float, input().split()))
x = pontos[0]
y = pontos[1]

if x == 0 and y == 0: print('Origem')
elif x == 0: print('Eixo Y')
elif y == 0: print('Eixo X')
else:
    if(x > 0):
        if(y > 0): print('Q1')
        else: print('Q4')
    else:
        if(y > 0): print('Q2')
        else: print('Q3')
