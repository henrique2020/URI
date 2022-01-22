unidade = ['I', 'X', 'C', 'M'] ## Unidades que variam 
unidade_meio = ['V', 'L', 'D'] ## Unidades da metade do valor
numeral = input()
numeral_romano = ''
numeral = numeral[::-1]
for x in range(len(numeral)-1, -1, -1):
    if numeral[x] == '1':
        numeral_romano+=unidade[x]
    elif numeral[x] == '2':
        numeral_romano+=unidade[x]+unidade[x]
    elif numeral[x] == '3':
        numeral_romano+=unidade[x]+unidade[x]+unidade[x]
    elif numeral[x] == '4':
        numeral_romano+=unidade[x]+unidade_meio[x]
    elif numeral[x] == '5':
        numeral_romano+=unidade_meio[x]
    elif numeral[x] == '6':
        numeral_romano+=unidade_meio[x]+unidade[x]
    elif numeral[x] == '7':
        numeral_romano+=unidade_meio[x]+unidade[x]+unidade[x]
    elif numeral[x] == '8':
        numeral_romano+=unidade_meio[x]+unidade[x]+unidade[x]+unidade[x]
    elif numeral[x] == '9':
        numeral_romano+=unidade[x]+unidade[x+1]
print(numeral_romano)