for _ in range(int(input())):
    comands = []
    for _ in range(int(input())):
        c = input()
        if 'SAME' in c:
            c = c.replace('SAME AS ', '')
            comands.append(comands[int(c)-1])
        else: comands.append(c)

    print(comands.count('RIGHT') - comands.count('LEFT'))
