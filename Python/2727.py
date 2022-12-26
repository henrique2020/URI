while True:
    try:
        for _ in range(int(input())):
            entrada = input().split()
            pontos = len(entrada[0])
            grupos = (len(entrada) - 1) * 3
            
            decod = chr(96+(pontos + grupos))
            print(decod)
            
    except: break
