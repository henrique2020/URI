anoes = 0 #A
elfos = 0 #E
humanos = 0 #H
magos = 0 #M
hobbits = 0 #X

#Entrada
repeticoes = int(input())
x = 0
while x < repeticoes:
    #Entrada
    aliado = input().split()
    nome, raca = aliado
    if raca == "A":
        anoes+=1
    elif raca == "E":
        elfos+=1
    elif raca == "H":
        humanos+=1
    elif raca == "M":
        magos+=1
    else:
        hobbits+=1
    x+=1
#Saida
print("%d Hobbit(s)" %hobbits)
print("%d Humano(s)" %humanos)
print("%d Elfo(s)" %elfos)
print("%d Anao(s)" %anoes)
print("%d Mago(s)" %magos)
