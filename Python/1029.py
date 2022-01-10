rep = int(input())
while rep:
    f = int(input())
    fib = int((((((1+(5**0.5))/2)**f)-(((1-(5**0.5))/2)**f))/(5**0.5)))
    calc = 0
    for g in range(f-1, 0, -1):
        calc += 2*int((((((1+(5**0.5))/2)**g)-(((1-(5**0.5))/2)**g))/(5**0.5)))
    print(f'fib({f}) = {calc} calls = {fib}')
    rep-=1
