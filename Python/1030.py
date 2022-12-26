rep = int(input())
for case in range(rep):
    pessoas, saltos = map(int, input().split())
    pos = 0
    pList = []
    [pList.append(x) for x in range(1, pessoas+1)]
    
    while(len(pList) > 1):
        pos += saltos - 1
        while(pos >= len(pList)): pos -= len(pList)
        del (pList[pos])
        
    print('Case {}: {}'.format(case+1, pList[0]))
