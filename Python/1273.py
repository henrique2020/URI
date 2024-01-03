fimDeLinha = False
while True:
    n = int(input())
    if n == 0: break

    if fimDeLinha: print()

    palavras = []
    caracteres = 0

    for _ in range(n):
        palavra = input()
        palavras.append(palavra)
        if len(palavra) > caracteres: 
            caracteres = len(palavra)

    for palavra in palavras:
        print(palavra.rjust(caracteres))

    fimDeLinha = True