def imprimir(arr, tipo):
    if tipo == 'p':
        for x in range(5):
            print('par[{}] = {}'.format(x, arr[x]))
    else:
        for x in range(5):
            print('impar[{}] = {}'.format(x, arr[x]))
        
par = []
impar = []
for x in range(15):
    n = int(input())
    if n%2 == 0:
        par.append(n)
        if len(par) == 5:
            t = 'p'
            imprimir(par, t)
            par.clear()
    else:
        impar.append(n)
        if len(impar) == 5:
            t = 'i'
            imprimir(impar, t)
            impar.clear()

for x in range(len(impar)):
    print('impar[{}] = {}'.format(x, impar[x]))

for x in range(len(par)):
    print('par[{}] = {}'.format(x, par[x]))