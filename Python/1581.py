rep = int(input())
for _ in range(rep):
    linguas = []
    for x in range(int(input())):
        linguas.append(input())
    
    if len(set(linguas)) == 1:
        print(linguas[0])
    else: print('ingles')
