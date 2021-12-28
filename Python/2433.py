pred = list(map(int, input().split()))
dis_pred = list(map(int, input().split()))
dis_pred.sort()

restam = pred[0]-pred[1]

soma = dis_pred[(restam-1)] - dis_pred[0]
distancia = soma

for x in range(1, pred[1]):
    soma = dis_pred[x+(restam-1)] - dis_pred[x]
    if(soma < distancia):
        distancia = soma

print(distancia)
