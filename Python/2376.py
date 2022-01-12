copa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
for x in range(15):
    t1, t2 = map(int, input().split())
    if t1>t2:
        copa.append(copa[x*2])
    else:
        copa.append(copa[x*2+1])

print(copa[-1])
