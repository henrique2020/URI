rep = int(input())
for _ in range(rep):
    numero = sorted(list(input()))
    if '0' in numero:
        pos = numero.count('0')
        numero[0] = numero[pos]
        numero[pos] = '0'
    #[print(n, end='') for n in numero]
    #print()
    print(''.join(numero))
