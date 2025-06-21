conteiner = list(map(int, input().split()))
navio = list(map(int, input().split()))

print(
    (navio[0] // conteiner[0]) *
    (navio[1] // conteiner[1]) *
    (navio[2] // conteiner[2])
)
