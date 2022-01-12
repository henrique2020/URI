while True:
    entrada = int(input())
    if entrada == 0:
        break
    lista = list(range(1, entrada+1))
    print(' '.join(map(str, lista))) ##.join() aceita apenas 'str'
