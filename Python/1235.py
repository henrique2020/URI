for _ in range(int(input())):
    s = input()
    metade = (len(s)//2) - 1
    
    pos = 0
    while (metade - pos >= 0):
        print(s[metade - pos], end='')
        pos += 1

    pos = 0
    while (metade + pos < len(s)-1):
        print(s[len(s)-1 - pos], end='')
        pos += 1
    
    print()