valor = 0

x = 0
while x < 2:
	linha = input().split()
	a, b, c = linha
	cod = int(a)
	qtde = int(b)
	preco = float(c)
	
	valor+= (qtde*preco)
	x+=1
print("VALOR A PAGAR: R$ %.2f" %valor)
