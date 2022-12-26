for _ in range(int(input())):
    tomadas = list(map(int, input().split()))
    reguas = tomadas[0]
    print(sum(tomadas[1:]) - (reguas-1))    #Uma régua se conecta na outra
