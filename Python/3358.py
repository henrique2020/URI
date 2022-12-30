vogais = ['a', 'e', 'i', 'o', 'u']
rep = int(input())
for _ in range(rep):
    sobrenome = input()
    consoantes_consecutivas = 0
    facil = True
    for letra in sobrenome.lower():
        if letra not in vogais: 
            consoantes_consecutivas += 1
            if consoantes_consecutivas == 3: 
                facil = False
                break
        else:
            consoantes_consecutivas = 0

    if facil: print('{} eh facil'.format(sobrenome))
    else: print('{} nao eh facil'.format(sobrenome))
