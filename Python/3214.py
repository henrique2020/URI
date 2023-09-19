# p = garrafas em posse
# e = garrafas encontradas
# n = garrafas necessárias
p, e, n = map(int, input().split())

g = p + e
trocas = 0
while (g >= n):
    t = g//n
    trocas += g//n
    
    g = g%n + t

print(trocas)
