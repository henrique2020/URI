kilo = 1000
valor_kilo = []
for _ in range(int(input())):
    valor, gramas = map(float, input().split())
    valor_kilo.append(valor * kilo / gramas)

print(f"{min(valor_kilo):.2f}")