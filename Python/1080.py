rep = 100
lista = []
while rep:
    lista.append(int(input()))
    
    rep -= 1

print(max(lista))
print(lista.index(max(lista))+1)
