qtde_pessoas_roda, qtde_garrafa, qtde_cuia = map(float, input().split())
pessoas_roda = input().split()

cuias = qtde_garrafa//qtde_cuia
if qtde_garrafa % qtde_cuia == 0: cuias -= 1
    
rico_mate = int(cuias%qtde_pessoas_roda)
agua_cuia = qtde_garrafa - qtde_cuia*cuias
print('{} {:.1f}'.format(pessoas_roda[rico_mate], agua_cuia))
