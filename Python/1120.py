while True:
    d, n = map(int, input().split())
    if d == 0 and n == 0: break

    valor = str(n).replace(str(d), '')
    if valor == '': valor = '0'
    print(int(valor))
