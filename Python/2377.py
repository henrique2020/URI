tamanho, distancia = map(int, input().split())
valor_km, valor_pedagio = map(int, input().split())
print((valor_km*tamanho)+(valor_pedagio*(tamanho//distancia)))
