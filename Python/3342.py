from math import ceil, floor

tamanho = int(input())**2
brancas = ceil(tamanho/2)
pretas = floor(tamanho/2)

print(f'{brancas} casas brancas e {pretas} casas pretas')
