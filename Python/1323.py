while True:
    n = int(input())
    if n == 0:
        break
    quadrados = 0
    for x in range(1, n+1):
        quadrados += x*x
    print(quadrados)