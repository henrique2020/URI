for _ in range(int(input())):
    t = int(input())
    tiros = list(map(int, input().split()))
    movimentos = input()

    acertos = 0
    for i in range(t):
        if(tiros[i] <= 2 and movimentos[i] == 'S') or (tiros[i] >= 3 and movimentos[i] == 'J'):
            acertos += 1
    
    print(acertos)