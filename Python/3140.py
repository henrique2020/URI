# Problema: 3140 - Copiando e Colando Código | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]               | Tempo: 0.356s

save = False
while True:
    try: 
        line = input()
        if "body>" in line: 
            save = not save
            if not save: break
            else: continue
        if save: print(line)
    except EOFError:
        break
