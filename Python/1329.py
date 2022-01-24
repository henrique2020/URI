while True:
    jogos = int(input())
    if jogos == 0:
        break
    moeda = input().split()
    print('Mary won %d times and John won %d times' % (moeda.count('0'), moeda.count('1')))
