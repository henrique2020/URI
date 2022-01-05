linha = input().split()
a, b = linha

a = int(a)
b = int(b)
resto = a%abs(b)
quociente = (a-resto)/b

print("{:d} {:d}".format(round(quociente), resto))
