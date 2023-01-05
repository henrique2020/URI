for _ in range(int(input())):
    n_sorte = list(input().replace('\r', ''))
    n_sorte.sort()
    
    pos = n_sorte.count('0')
    if pos:
        temp = n_sorte[pos]
        n_sorte[0] = temp
        n_sorte[pos] = '0'
        
    print(''.join(n_sorte))
