## Primeira versão - 0.316s
linha = input().split()
a, b = linha

a = int(a)
b = int(b)
resto = a%abs(b)
quociente = (a-resto)/b

print("{:d} {:d}".format(round(quociente), resto))

##Segunda versão - 0.024s
a, b = map(int, input().split())
resto = a%abs(b)
quociente = int((a-resto)/b)

print(quociente, resto)
