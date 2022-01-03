simulacoes = int(input())
ganhou = 0
while simulacoes:
    car = int(input())
    if car != 1:
        ganhou+=1
    simulacoes -= 1
print(ganhou)
