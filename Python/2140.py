notas = [2, 5, 10, 20, 50, 100]

trocos_possiveis = []
for n1 in notas:
    for n2 in notas:
        trocos_possiveis.append(n1+n2)

while True:
    vc, vp = map(int, input().split())
    if vc == vp == 0: break
    
    if (vp - vc) in trocos_possiveis: print('possible')
    else: print('impossible')
