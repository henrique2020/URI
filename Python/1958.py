valor = input()

if valor[0] == '-':
    valor = float(valor)
    print('{:.4E}'.format(valor))
else:
    valor = float(valor)
    print('+{:.4E}'.format(valor))
