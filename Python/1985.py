tabelaPrecos = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

conta = 0
for _ in range(int(input())):
    id, qtde = map(int, input().split())
    conta += tabelaPrecos[id] * qtde

print(f"{conta:0.2f}")
