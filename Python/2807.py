entrada = int(input())
fibonacci = []
for g in range(1, entrada+1):
    fibonacci.append(int((((((1+(5**0.5))/2)**g)-(((1-(5**0.5))/2)**g))/(5**0.5))))
print(' '.join(map(str, fibonacci[::-1])))
