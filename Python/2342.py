overflow = int(input())
n1, sinal, n2 = input().split()

if sinal == '+': calc = int(n1) + int(n2)
elif sinal == '*': calc = int(n1) * int(n2)

if calc <= overflow: print('OK')
else: print('OVERFLOW')
