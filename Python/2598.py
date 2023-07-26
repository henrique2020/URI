for _ in range(int(input())):
    tam, km = map(int, input().split())
    radares = tam // km
    if(tam % km != 0): radares += 1
    print(radares)