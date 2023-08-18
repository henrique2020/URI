for _ in range(int(input())):
    b = int(input())
    
    aD, dD, lD = map(int, input().split())
    vD = (aD+dD) / 2
    if lD % 2 == 0: vD += b
    
    aG, dG, lG = map(int, input().split())
    vG = (aG+dG) / 2
    if lG % 2 == 0: vG += b
    
    if(vD > vG): print("Dabriel")
    elif(vD < vG): print("Guarte")
    else: print("Empate")