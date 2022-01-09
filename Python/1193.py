## A conversão funciona normalmente, mas...
# Ao converter para binario vem os caracateres '0b' na frente
# Ao converter para hexadecimal vem os caracateres '0x' na frente
## Por isso foi usado do modo mais em baixo
'''
rep = int(input())
for x in range (1, rep+1):
	num, type = map(str, input().split())
	print("Case {}:".format(x))
	if type == 'bin':
		print("{} dec".format(int(num, 2)))
		print("{} hex".format(hex(int(num, 2))))
	elif type == 'dec':
		print("{} hex".format(hex(int(num))))
		print("{} bin".format(bin(int(num))))
	else:
		print("{} dec".format(int(num, 16)))
		print("{} bin".format(bin(int(num, 16))))
	print()
'''

## Versão com a conversão direta sem caracteres a mais
rep = int(input())
for x in range (1, rep+1):
	num, type = map(str, input().split())
	print("Case {}:".format(x))
	if type == 'bin':
		print("{} dec".format(format(int(num, 2), 'd')))
		print("{} hex".format(format(int(num, 2), 'x')))
	elif type == 'dec':
		print("{} hex".format(format(int(num), 'x')))
		print("{} bin".format(format(int(num), 'b')))
	else:
		print("{} dec".format(format(int(num, 16), 'd')))
		print("{} bin".format(format(int(num, 16), 'b')))
	print()
