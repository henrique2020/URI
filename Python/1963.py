antes, depois = map(float, input().split())

if antes == depois: print('%.02f%%' % 0)
else:
    aumento = depois - antes

    aumento = 100 / (antes / aumento)
    print('%.02f%%' % aumento)