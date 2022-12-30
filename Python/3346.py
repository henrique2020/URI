f1, f2 = map(float, input().split())
f1 = (1.0 + f1/100) #Cacula o % de f1
f2 = (1.0 + f2/100) #Cacula o % de f2
flutuacao = ((f1*f2)-1) #Remove os "100%" do PIB (no caso 1)
flutuacao = flutuacao*100   #Faz com que 100% se torne 1, ou seja, 0.8 equivale a 80%
print("%.6f" % flutuacao)
