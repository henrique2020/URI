# Problema: 3140 - Copiando e Colando Código | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]               | Tempo: 0.558s

save = False
while True:
    try: 
        line = input()
        if "body>" in line: 
            save = not save
            continue
        if save: print(line)
    except EOFError:
        break
