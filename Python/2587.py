for x in range(int(input())):
    p1 = input()
    p2 = input()
    p = input() #palavra incompleta

    pos = []
    for x in range(len(p)):
        if p[x] == '_': pos.append(x)


    if ((p1[pos[0]] == p2[pos[1]])
        or (p1[pos[1]] == p2[pos[0]])
        or (p1[pos[0]] == p2[pos[0]] and p1[pos[1]] == p2[pos[1]])
        ): print('Y')
    else: print('N')