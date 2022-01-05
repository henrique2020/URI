while True:
    percorrer = list(map(int, input().split()))
    if min(percorrer) <= 0:
        break

    soma = 0
    numbers = []
    for x in range(min(percorrer), max(percorrer)+1):
        numbers.append(str(x))
        soma += x
    print(' '.join(numbers), 'Sum={}'.format(soma))
