entradas, saldo = map(int, input().split())

menorSaldo = saldo
for _ in range(entradas):
    saldo += int(input())
    if saldo < menorSaldo: menorSaldo = saldo

print(menorSaldo)
