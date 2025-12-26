# Problema: 1608 - Bolos da Maria | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]    | Tempo: 0.234s


for _ in range(int(input())):
    d, i, b = map(int, input().split())
    precos = list(map(int, input().split()))
    bolos = [list(map(int, input().split()))[1:] for _ in range(b)]
    
    total = []
    for bolo in bolos:
        gastos = 0
        for pos in range(0, len(bolo), 2):
            valor = precos[bolo[pos]] * bolo[pos+1]
            if d >= gastos + valor: gastos += valor
            else: break
            
            if pos+2 == len(bolo):
                total.append(1 * d//gastos)

    print(max(total) if total else 0)
