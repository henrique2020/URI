input()
carneiros = list(map(int, input().split()))
p = 0
carneiros_totais = sum(carneiros)
carneiros_roubados = 0
estrelas_visitadads = []
while True:
    if p < 0 or p > len(carneiros)-1: break
    proximo = 1 if carneiros[p] % 2 != 0 else -1
    
    if p not in estrelas_visitadads: estrelas_visitadads.append(p)
    
    if carneiros[p] != 0:
        carneiros_roubados += 1
        carneiros[p] -= 1
        
    p += proximo
    
print(len(estrelas_visitadads), (carneiros_totais - carneiros_roubados))