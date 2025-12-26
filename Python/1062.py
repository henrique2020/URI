# Problema: 1062 - Trilhos     | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.442s

while True:
    vagoes = int(input())
    if vagoes == 0: break
    
    while True:
        gabarito = list(map(int, input().split()))
        if len(gabarito) == 1 and gabarito[0] == 0:
            print()
            break
        
        parado = []
        proximo_vagao = 1
        possivel = True
        
        for esperado in gabarito:
            while proximo_vagao <= vagoes and (not parado or parado[-1] != esperado):
                parado.append(proximo_vagao)
                proximo_vagao += 1
            
            if parado and parado[-1] == esperado:
                parado.pop()
                
            else:
                possivel = False
                break
        
        if possivel: print("Yes")
        else: print("No")
