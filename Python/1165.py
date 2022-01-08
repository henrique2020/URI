def verificaPrimo(numero):
    info = True
    start = 2

    if numero == 1 or numero == 0:
        info = False

    else:
        while(start <= numero/2):
            if numero % start == 0:
                info = False
                break
            start += 1
    return info

rep = int(input())
while rep:
    num = int(input())
    if(verificaPrimo(num)):
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')
    rep-=1