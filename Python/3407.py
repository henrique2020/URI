n_itens, n_bolinhos_doce = map(int, input().split())
bolinhos_doce_Natan = input().split()
bolinhos_doce_Samuel = input().split()

if bolinhos_doce_Natan.count('1') == n_bolinhos_doce: print("Tudo certo.")
elif bolinhos_doce_Samuel.count('1') == n_bolinhos_doce: print("Pegou de Samuel.")
else: print("Pegou de um estranho.")
