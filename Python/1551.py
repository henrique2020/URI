# Problema: 1551 - Frase Completa | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]    | Tempo: 0.000s

for _ in range(int(input())):
    letters = set()
    string = input().lower()
    
    letters = {c for c in string if c.isalpha()}
    
    if(len(letters) == 26): print("frase completa")
    elif(len(letters) >= 13): print("frase quase completa")
    else: print("frase mal elaborada")