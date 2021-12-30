## Caso de teste 1
while True:
    ini, fim = map(int, input().split())
    if (ini == 0 and fim == 0):
        break

    count = {
        '0':0,
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0
        }
        
    for x in range(ini, fim+1):
        num = list(map(str, str(x)))
        for c in num:
            count[c]+=1
    
    print('%d %d %d %d %d %d %d %d %d %d' % (count['0'], count['1'], count['2'], count['3'], count['4'], count['5'], count['6'], count['7'], count['8'], count['9']))
    
    
    
## Caso de teste 2
while True:
    ini, fim = map(int, input().split())
    if (ini == 0 and fim == 0):
        break

    count = [0,0,0,0,0,0,0,0,0,0]  
    for x in range(ini, fim+1):
        num = list(map(str, str(x)))
        for c in num:
            count[int(c)]+=1
    
    print('%d %d %d %d %d %d %d %d %d %d' % (count[0], count[1], count[2], count[3], count[4], count[5], count[6], count[7], count[8], count[9]))

    
    
## Caso de teste 3
while True:
    ini, fim = map(int, input().split())
    if (ini == 0 and fim == 0):
        break

    num = []
    for x in range(ini, fim+1):
        num += list(map(int, str(x)))

    print('%d %d %d %d %d %d %d %d %d %d' % (num.count(0), num.count(1), num.count(2), num.count(3), num.count(4), num.count(5), num.count(6), num.count(7), num.count(8), num.count(9)))
