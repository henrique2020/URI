rep = int(input())
for instancia in range(1, rep+1):
    frase = input()
    t1 = input()
    t2 = input()
    
    pt1, pt2, desempate = 0, 0, None
    for p in range(len(frase)):
        if frase[p] == t1[p]: pt1 += 1
        if frase[p] == t2[p]: pt2 += 1

        if not desempate:
            if frase[p] == t1[p] and frase[p] != t2[p]: desempate = '1'
            elif frase[p] == t2[p] and frase[p] != t1[p]: desempate = '2'
    
    print(f"Instancia {instancia}")
    if pt1 > pt2 or (pt1 == pt2 and desempate == '1'): print("time 1")
    elif pt1 < pt2 or (pt1 == pt2 and desempate == '2'): print("time 2")
    else: print("empate")
    print()
