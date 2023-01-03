consumo = int(input())
conta = 7

if consumo > 100:
    conta += 20*1   #Consumo entre 11 e 30L
    conta += 70*2   #Consumo entre 31 e 100L
    conta += (consumo-100)*5    #Consumo acima de 100L
elif consumo > 30:
    conta += 20*1   #Consumo entre 11 e 30L
    conta += (consumo-30)*2
elif consumo > 10:
    conta += (consumo-10)

print(conta)
