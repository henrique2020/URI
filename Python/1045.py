pontos = list(map(float, input().split()))
pontos.sort(reverse=True)
a = pontos[0]
b = pontos[1]
c = pontos[2]

if(a >= (b+c)):
    print('NAO FORMA TRIANGULO')
else:
    if((a*a) == (b*b+c*c)):
        print('TRIANGULO RETANGULO')
    elif((a*a) > (b*b+c*c)):
        print('TRIANGULO OBTUSANGULO')
    else: #((a*a) < (b*b+c*c))
        print('TRIANGULO ACUTANGULO')
    
    if(a == b and b == c):
        print('TRIANGULO EQUILATERO')
    elif(a == b or b == c or c == a):
        print('TRIANGULO ISOSCELES')
