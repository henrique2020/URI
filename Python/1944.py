face = ['F', 'A', 'C', 'E']
ganhadores = 0
frase = [face]
for _ in range(int(input())):
    letras = input().split()
    if letras[::-1] == frase[-1]:
        ganhadores += 1
        del frase[-1]
        if len(frase) == 0: frase.append(face)
    else:
        frase.append(letras)

print(ganhadores)
