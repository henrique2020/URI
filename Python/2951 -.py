inicio = input().split()
nRunas, vida = inicio

nRunas = int(nRunas)
vida = int(vida)

runa = []
dano = []

x=0
while x<nRunas:
    linha = input().split()
    runa.append(linha[0]), dano.append(int(linha[1]))
    x+=1

runasUsadas = int(input())
tiposUsadas = input().split()

danoCausado = 0
y = 0
while y<nRunas:
    if runa[y] in tiposUsadas:
        danoCausado+=dano[y]
    y+=1

print("%d" %danoCausado)
if danoCausado < vida:
    print("My precioooous")
else:
    print("You shall pass!")
