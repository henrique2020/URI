linha = input().split()
distancia, comprimento = linha

distancia = int(distancia)
comprimento = int(comprimento)

print("%d"%(distancia%comprimento))
