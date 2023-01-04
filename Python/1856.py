input()
inimigos = input().split()
rep = int(input())
for _ in range(rep):
    dados = input().split()
    op = dados[0]
    
    if(op == 'I'):
        p = dados[1]
        e = dados[2]
        inimigos.insert(inimigos.index(e)+1, p)
    elif(op == 'R'):
        e = dados[1]
        inimigos.remove(e)
    else:
        ini = dados[1]
        fim = dados[2]
        print('{:d}'.format(abs(inimigos.index(ini) - inimigos.index(fim))-1))

        
