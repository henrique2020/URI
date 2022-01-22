altPulo, qtdCanos = map(int, input().split())
canos = list(map(int, input().split()))
win = True
for x in range(0, qtdCanos-1):
    if(abs(canos[x]-canos[x+1]) > altPulo):
        win = False
        break
if win: print('YOU WIN')
else: print('GAME OVER')