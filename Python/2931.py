d_entrega, d_final = map(int, input().split())

if(d_entrega > d_final or d_entrega >= 25): print("Eu odeio a professora!")
elif(d_entrega+3 <= d_final): print("Muito bem! Apresenta antes do Natal!")
else: 
    print("Parece o trabalho do meu filho!")
    if(d_entrega+2 < 24): print("TCC Apresentado!")
    else: print("Fail! Entao eh nataaaaal!")
