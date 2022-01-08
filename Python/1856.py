'''
    { TIME LIMIT EXCEEDED }
'''
##Modelo 1
def add(p, e):
    for x in lista:
        if(x == e):
            lista.insert(lista.index(x)+1, p)
            break

def delete(e):
    lista.remove(e)

def quantidade(ini, fim):
    posIni = lista.index(ini)
    posFim = lista.index(fim)
    if(posIni > posFim):
        dif = posIni-1 - posFim
    else:
        dif = posFim-1 - posIni
    results.append(dif)
    print('{:d}'.format(dif))

inimigos = int(input())
lista = input().split()
operacoes = int(input())
results = []
for rep in range(operacoes):
    dados = input().split()

    if(dados[0] == 'I'):
        add(dados[1], dados[2])
    elif(dados[0] == 'R'):
        delete(dados[1])
    else:
        quantidade(dados[1], dados[2])

##Modelo de teste 2
'''
inimigos = int(input())
lista = input().split()
operacoes = int(input())
for rep in range(operacoes):
    dados = input().split()
    if(dados[0] == 'I'):
        lista.insert(lista.index(dados[2])+1, dados[1])
    elif(dados[0] == 'R'):
        lista.remove(dados[1])
    else:
        posIni = lista.index(dados[1])
        posFim = lista.index(dados[2])
        if(posIni > posFim):
            dif = posIni-1 - posFim
        else:
            dif = posFim-1 - posIni
        print('%d' % dif)
'''