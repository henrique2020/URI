while True:
    try: codigos = int(input())
    except: break
    
    lista = []
    for _ in range(codigos):
        lista.append(input())
        
    lista.sort()
    print("\n".join(lista))
