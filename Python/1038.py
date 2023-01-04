tabela = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}
cod, qtde = map(int, input().split())
print("Total: R$ %.2f" % (tabela[cod] * qtde))
