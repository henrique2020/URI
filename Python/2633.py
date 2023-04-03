while True:
    try: carnes = int(input())
    except: break
    
    lista = []
    for _ in range(carnes):
        carne, peso = input().split()
        lista.append((int(peso), carne))
    
    lista.sort(key=lambda peso:peso[0])
    print(" ".join(a[1] for a in lista))