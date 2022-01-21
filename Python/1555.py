for x in range(int(input())):
    x, y = map(int, input().split())
    r = (3*x)**2 + y**2 #Poderia ter usado o pow() ao invés de **
    b = 2*(x**2) + (5*y)**2
    c = -100*x +y**3
    if r > b and r > c:
        nome = 'Rafael'
    elif b > r and b > c:
        nome = 'Beto'
    #elif c > r and c > b: #Supoem-se que nunca haverá empate, então...:
    else:
        nome = 'Carlos'
    print('{} ganhou'.format(nome))