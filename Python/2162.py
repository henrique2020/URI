def verifica(n1, n2, status):
    if status == 'maior' and n1 < n2: return 'menor'
    elif status == 'menor' and n1 > n2: return 'maior'
    
    return False


input()
alt = list(map(int, input().split()))
padrao = 1

if alt[0] == alt[1]: print(0)
else:
    if alt[0] < alt[1]: status = 'menor'
    elif alt[0] > alt[1]: status = 'maior'

    for x in range(2, len(alt)):
        status = verifica(alt[x-1], alt[x], status)
        if not status:
            padrao = 0
            break

    print(padrao)
