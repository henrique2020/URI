j, r = map(int, input().split())
pontosV = [ 0 for _ in range(j)]

pontosE = map(int, input().split())
for n, p in enumerate(pontosE):
    pontosV[n%j] += p

maxP = max(pontosV)
lp = 0
for n, p in enumerate(pontosV):
    if p == maxP:
        lp = n

print(lp+1)
