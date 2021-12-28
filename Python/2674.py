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

while True:
    try: n = abs(int(input()))
    except: break
    num = list(map(int, str(n)))

    primo = False
    if(verificaPrimo(n)):
        primo = True
        super = True
        for x in num:
            if(verificaPrimo(x) is False):
                super = False
                break

    if(primo):
        if(super):
            print('Super')
        else:
            print('Primo')
    else:
        print('Nada')
