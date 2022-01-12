rep = int(input())
while rep:
    n = list(map(int, input().split()))
    alunos = n[0]
    notas = n[1:]
    total = 0
    for x in range(0, alunos):
        total += notas[x]
    media = total/alunos

    qtde = 0
    for x in range(0, alunos):
        if media < notas[x]:
            qtde += 1
    print('%.3f%%' %(qtde*100/alunos))
    rep -= 1
