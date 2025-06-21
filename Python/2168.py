quadras = int(input())
cameras = []
for _ in range(quadras+1):
    cameras.append(list(map(int, input().split())))

for p1 in range(quadras):
    for p2 in range(quadras):
        esquinas = [cameras[p1][p2], cameras[p1][p2+1], cameras[p1+1][p2], cameras[p1+1][p2+1]]
        print('S' if esquinas.count(1) >= 2 else 'U', end='')
    print()