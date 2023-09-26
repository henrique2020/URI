saida = []
while True:
    try: d1, d2, rep = map(int, input().split())
    except: break

    for _ in range(rep):
        dp1, dp2 = map(int, input().split())
        if(dp1 <= d1 and dp2 <= d2):
            saida.append("Sim")
        elif(dp1 <= d2 and dp2 <= d1):
            saida.append("Sim")
        else:
            saida.append("Nao")
            
print("\n".join(saida))