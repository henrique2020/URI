lutas = int(input())
vitorias = lutas

for _ in range(lutas):
    if('CD' in input()):
        vitorias -= 1

print(vitorias)
