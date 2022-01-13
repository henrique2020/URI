while True:
    try: tam = int(input())+1
    except: break
    
    for x in range(1, tam):
        line = ''
        for y in range(1, tam):
            if x+y == tam:
                line+='2'
            elif x == y:
                line+='1'
            else:
                line+='3'
        print(line)
