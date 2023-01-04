rep = int(input())
for _ in range(rep):
    entrada = input().replace('.', '')
    diamantes = 0
    while ((busca := entrada.count('<>'))):
        diamantes += busca
        entrada = entrada.replace('<>', '')
    print(diamantes)
