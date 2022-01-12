soma = 0
rep = 2
while rep:
    n = float(input())
    if n >= 0 and n <= 10:
        soma+=n
        rep-=1
    else:
        print('nota invalida')

print('media = %.2f' % (soma/2))
