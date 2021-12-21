list_vogal = ['a', 'e', 'i', 'o', 'u']

##Runtime Error

nome = ''
lista = []
vogais = 0
consoantes = 0
distintas = []

rep = int(input())
while (rep):
    tamanho = input()
    nome_lista = ''
    while(tamanho):
        titulo = input().lower()
        nome_lista += titulo[0]
        if titulo[0] not in distintas:
            distintas.append(titulo[0])
            if titulo[0] in list_vogal: vogais += 1
            else: consoantes += 1

        tamanho -= 1

    lista.append(nome_lista)
    nome += nome_lista[0].upper()
    rep -= 1
    
print("Nome da Linguagem: %s" % nome)
print("Lista de Palavras:")
for palavra in lista:
    print(palavra)
print("Numero de Vogais: %d" % vogais)
print("Numero de Consoantes: %d" % consoantes)
print("Numero Total de Letras: %d" % (vogais + consoantes))
if consoantes != 0:
    print("Tempo para aprender: %.1f horas" % ((len(distintas)+vogais)/consoantes))
else:
    print("Linguagem Ruim")
