while True:
    try:
        degraus = int(input())
        h, c, l = map(int, input().split())
    except: break

    comprimento = degraus * (((h**2)+(c**2))**0.5) / 100
    largura = l / 100

    print("%.04f" % (comprimento*largura))
