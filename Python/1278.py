inicio = True
while True:
    palavras = int(input())
    if palavras == 0: break
    
    if(not inicio): print()
    
    entradas = []
    maxLen = 0
    for _ in range(palavras):
        e = input().split()
        e = " ".join(e)
        entradas.append(e)
        
        if len(e) > maxLen: maxLen = len(e)
    
    for frase in entradas:
        spaces = ' ' * (maxLen - len(frase))
        print('{}{}'.format(spaces, frase))
    
    inicio = False