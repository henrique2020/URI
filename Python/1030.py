#Incompletop
rep = int(input())
for case in range(0,rep):
    pessoas, saltos = map(int, input().split())
    pList = []
    for x in range(1, pessoas+1):
        pList.append(x)
    
    pos = saltos-1
    print(pList, len(pList), pos)
    while(len(pList) > 1):
        if len(pList)-1 > pos: pos+= saltos-1
        if len(pList)-1 <= pos: pos = pos%len(pList)
        
        #print(pList[pos-1], len(pList), pos)
        del (pList[pos-1])
        
    print('Case {}: {}'.format(case+1, pList[0]))
            