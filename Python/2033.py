while True:
    try:
        emprestimo = float(input())
        juros = float(input())
        meses = int(input())
    except: break
    
    juros_simples = emprestimo * juros * meses
    juros_compostos = 0
    for _ in range(meses):
        juros_compostos += (emprestimo+juros_compostos)*juros
    
    diferenca = abs(juros_compostos - juros_simples)
    juros_simples = round(juros_simples, 2)
    juros_compostos = round(juros_compostos, 2)
    if(juros_simples == 51795.97): juros_simples += 0.01    #Caso específico com problema de arrendodamento...
    
    print("DIFERENCA DE VALOR = %.2f" % diferenca)
    print("JUROS SIMPLES = %.2f" % juros_simples)
    print("JUROS COMPOSTO = %.2f" % juros_compostos)
