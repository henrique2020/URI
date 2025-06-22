figurinhas = int(input())
cartas = int(input())
possui = set(int(input()) for _ in range(cartas))
print(figurinhas - len(possui))