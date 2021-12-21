while True:
    filhos, filhas = input().split()
    filhos = int(filhos)
    filhas = int(filhas)
    
    if filhos == 0 and filhas == 0:
        break

    total = filhos + filhas
    print("%d" % total)
