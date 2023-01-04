from time import time
input()
inicio = time()
"""
while True:
    try:
        coluna = input()
        if not coluna: break
        tamanho = len(coluna)
        
        if tamanho > 3 or (tamanho == 3 and coluna > 'XFD'):
            print('Essa coluna nao existe Tobias!')
        else:
            indice = 0
            multiplicador = tamanho-1
            for e in coluna:
                indice+=(ord(e)-64)*26**multiplicador
                multiplicador-=1
            print(indice)
    except EOFError:
        break
"""

while True:
    try:
        coluna = input()
        if not coluna: break
        tamanho = len(coluna)
        
        if tamanho > 3 or (tamanho == 3 and coluna > 'XFD'):
            print('Essa coluna nao existe Tobias!')
        else:
            indice = 0
            for x in range(tamanho):
                indice+=(ord(coluna[x])-64)*26**(tamanho-(x+1))
            print(indice)
    except EOFError:
        break

"""
D={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26} 
while True:
    try:
        coluna = input()
        if not coluna: break
        tamanho = len(coluna)
        
        if tamanho > 3 or (tamanho == 3 and coluna > 'XFD'):
            print('Essa coluna nao existe Tobias!')
        else:
            indice = 0
            multiplicador = tamanho-1
            for e in coluna:
                indice+=D[e]*26**multiplicador
                multiplicador-=1
            print(indice)
    except EOFError:
        break
"""

fim = time()
print(inicio - fim)
