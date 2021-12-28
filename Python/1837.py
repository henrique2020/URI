linha = input().split()
a, b = linha

a = int(a)
b = int(b)

if a < 0:
    quociente = a//b
else:
    quociente = a/b
resto = a%abs(b)

print("{:d} {:d}".format(round(quociente), resto))
