rep = int(input())

while rep:
    notas = list(map(float, input().split()))
    media = notas[0]*0.2 + notas[1]*0.3 + notas[2]*0.5
    print('%.1f' % media)
    rep -= 1
