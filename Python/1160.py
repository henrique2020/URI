rep = int(input())
while rep:
    anos = 1
    result = True
    pop1, pop2, txc1, txc2 = map(float, input().split())
    for x in range(101):
        pop1 += int(pop1*(txc1/100))
        pop2 += int(pop2*(txc2/100))
        if pop1 > pop2:
            break
        anos+=1

    if anos <= 100:
        print(f'{anos} anos.')
    else:
        print('Mais de 1 seculo.')
    rep-=1