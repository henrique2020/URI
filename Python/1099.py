rep = int(input())
while rep:
    numbers = list(map(int, input().split()))
    soma = 0
    for x in range(min(numbers)+1, max(numbers)):
        if x%2 != 0:
            soma+=x
    print(soma)
    rep-=1
