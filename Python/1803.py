rep = 4
lista = []
while rep:
    lista.append(list(input()))
    rep-=1

tam = len(lista[0])-1
f = int(lista[0][0]+lista[1][0]+lista[2][0]+lista[3][0])
l = int(lista[0][-1]+lista[1][-1]+lista[2][-1]+lista[3][-1])
letter = ''
for x in range(1, tam):
    letter += chr((f*(int(lista[0][x]+lista[1][x]+lista[2][x]+lista[3][x]))+l)%257)
print(letter)
