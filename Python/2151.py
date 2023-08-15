for _ in range(int(input())):
    h, m, op = map(int, input().split())
    print(f'{h:02d}:{m:02d} - A porta {"abriu" if op == 1 else "fechou"}!')
