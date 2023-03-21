for _ in range(int(input())):
    senha = input()
    variacoes = 1
    
    for c in senha:
        if c.upper() in ['A', 'E', 'I', 'O', 'S']: variacoes *= 3
        else: variacoes *= 2
    
    print(variacoes)