pred = list(map(int, input().split()))
dis_pred = list(map(int, input().split()))
dis_pred.sort()

restam = pred[0]-pred[1]-1

soma = dis_pred[restam] - dis_pred[0]
distancia = soma

for x in range(1, pred[1]+1):
    soma = dis_pred[x+restam] - dis_pred[x]
    if(soma < distancia):
        distancia = soma

print(distancia)
