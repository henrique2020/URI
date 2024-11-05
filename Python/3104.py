a = input()
b = int(input())
resto = 0

for digito in a:
	resto = (resto * 10 + int(digito)) % b

print(resto)
