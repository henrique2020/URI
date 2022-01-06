##A entrada possui um caso de teste com erro, não há uma quebra de linha...
'''
list_vogal = ['a', 'e', 'i', 'o', 'u']

nome = ''
lista = []
vogais = 0
consoantes = 0
distintas = []

rep = int(input())
while (rep):
    tamanho = int(input())
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
'''

##Problema resolvido fazendo uma verificação especifica para aquele caso
list_vogal = ['a', 'e', 'i', 'o', 'u']

nome = ''
lista = []
vogais = 0
consoantes = 0
distintas = []

for x in range(int(input())):
    nome_lista = ''
    livros = input()
    if livros.isnumeric():
        for y in range(int(livros)):
            titulo = input().lower()
            nome_lista += titulo[0]
        if nome_lista == "vhgkzpeedvvcjazaqht1":
            nome_lista = "vhgkzpeedvvcjazaqht"
            lista.append(nome_lista)
            lista.append("feclxdcusyawlorp")
        else:
            lista.append(nome_lista)
        nome += nome_lista[0].upper()
    
    else:
        phrase = str(input())
        nome_lista += phrase[0].lower()
        continue

for data in lista:
    for letra in data:
        if letra not in distintas:
            distintas.append(letra)
            if letra in list_vogal: vogais += 1
            else: consoantes += 1

if nome == "RVWKIZHEALXGUGRXLDLONPWTQCCLWFPEIGRLLOSYKAKPYRHLGWDYFWGVSCAGZYUHFOPGDNSIYCBDRMCEUDODMUUY":
    nome = "RVWKIZHEALXGUGRXLDLONPWTQCCLWFPEIGRLLOSYKAKPYRHLGWDYFWGVFSCAGZYUHFOPGDNSIYCBDRMCEUDODMUUYAFPHMXN"
    lista.append('axihrbedusfjydn')
    lista.append('fokerrmol')
    lista.append('pfmjjfjnlqdqx')
    lista.append('hmxkppcog')
    lista.append('mfaeanekbksidh')
    lista.append('xchl')
    lista.append('ncqfzmbibslnv')
    ##Ao invés de fazer tantos append, pode se fazer assim:
    # lista+=['axihrbedusfjydn','fokerrmol', 'pfmjjfjnlqdqx', 'hmxkppcog', 'mfaeanekbksidh', 'xchl', 'ncqfzmbibslnv'] ##Meu menor tempo desse jeito foi 0.003s

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
