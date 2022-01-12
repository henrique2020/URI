def fib(num):
    for g in range(num):
        fib = int((((((1+(5**0.5))/2)**g)-(((1-(5**0.5))/2)**g))/(5**0.5)))
    return fib

rep = int(input())
while rep:
    num = int(input())
    print(f'Fib({num}) = {fib(num+1)}')
    rep-=1