# Problema: 1062 - Trilhos     | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 1.159s

vagoes = int(input())
while (vagoes != 0):
    while True:
        entrada = [n for n in range(1, vagoes+1)]
        gabarito = list(map(int, input().split()))
        if len(gabarito) == 1 and gabarito[0] == 0:
            print()
            break
        
        elif(entrada == gabarito or entrada == gabarito[::-1]):
            print("Yes")
        
        else:
            saida = []
            parado = []
            
            p = 0
            while p < vagoes:
                if len(entrada) > 0:
                    e = entrada[0]
                    entrada.remove(e)
                else: e = -1
                
                if e == gabarito[p]: 
                    saida.append(e)
                elif gabarito[p] in parado and parado[-1] == gabarito[p]:
                    saida.append(parado[-1])
                    parado.remove(parado[-1])
                    entrada.insert(0, e)
                elif e != -1:
                    parado.append(e)
                    continue
                
                p += 1
                    
            
            if(gabarito == saida): print("Yes")
            else: print("No")
    
    vagoes = int(input())
