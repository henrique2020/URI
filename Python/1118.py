calculo = True
while True:
    if calculo:
        rep = 2
        soma = 0
        while rep:
            n = float(input())
            if n >= 0 and n <= 10:
                soma+=n
                rep-=1
            else:
                print('nota invalida')
        print('media = %.2f' % (soma/2))
        calculo = False
    print('novo calculo (1-sim 2-nao)')
    novo = input()
    if(novo == '1'):
        calculo = True
    elif(novo == '2'):
        break
