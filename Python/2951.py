inicio = list(map(int, input().split()))
nRunas, vida = inicio
runa = {}
for x in range(nRunas):
    linha = input().split()
    runa[linha[0]] = int(linha[1])
    x+=1

input()
runasUsadas = input().split()

dano = 0
for x in runasUsadas:
    dano += runa[x]

print("%d" %dano)
if dano < vida:
    print("My precioooous")
else:
    print("You shall pass!")
