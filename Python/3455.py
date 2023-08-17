#3 questões de grafos (A) custam o mesmo que 2 questões de programação dinâmica (B) B -> A = *1.5
#2 questões de geometria (C) custam o mesmo que 5 questões de grafos (A) C -> A = *2.5
## C -> B = C -> A -> B = *2.5 / 1.5

from math import floor
a, b, c = map(int, input().split())
maximize = input().upper()

q = 0
if maximize == 'A':
    q = a + b*1.5 + c*2.5
elif maximize == 'B':
    q = b + (a + c*2.5) / 1.5
elif maximize == 'C':
    q = c + (a + b*1.5) / 2.5

print('{:.0f}'.format(floor(q)))