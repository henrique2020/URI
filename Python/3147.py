h, e, a, o, w, x = map(int, input().split())
bem = h+e+a+x+1
mal = o+w

if(bem > mal): print('Middle-earth is safe.')
else: print('Sauron has returned.')