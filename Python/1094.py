rep = int(input())
cobaias = 0
c = 0
r = 0
s = 0
while rep:
    entrada = input().split()
    cobaias += int(entrada[0])
    if entrada[1] == 'C':
        c += int(entrada[0])
    elif entrada[1] == 'R':
        r += int(entrada[0])
    else:
        s += int(entrada[0])
    rep -= 1

print('Total: %d cobaias' % cobaias)
print('Total de coelhos: %d' % c)
print('Total de ratos: %d' % r)
print('Total de sapos: %d' % s)
print('Percentual de coelhos: %.2f %%' % (c*100/cobaias))
print('Percentual de ratos: %.2f %%' % (r*100/cobaias))
print('Percentual de sapos: %.2f %%' % (s*100/cobaias))
