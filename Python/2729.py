[print(" ".join(sorted(set(input().split())))) for _ in range(int(input()))]

# Outras formas de fazer:
# 1
"""
for _ in range(int(input())):
    print(" ".join(sorted(set(input().split()))))
"""
# 2
"""
for _ in range(int(input())):
    lista = input().split()
    listaUnica = list(set(lista))
    print(" ".join(sorted(listaUnica)))
"""
