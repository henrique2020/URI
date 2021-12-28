x = 0
while True:
	instancia = input()
	y = int(instancia)
	if y == 0:
		break
	elif y != 0:
		if x >= 1:
			print()
		x+=1
		codigo = input()
		print("Instancia %d"%x)
		if instancia in codigo:
			print("verdadeira")
		else:
			print("falsa")
