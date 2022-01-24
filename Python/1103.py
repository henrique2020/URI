while True:
    h1, m1, h2, m2 = map(int, input().split())
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
    #if m1 > m2 and h1 < h2: m2 += 60
    if (h1 > h2) or (h1 == h2 and m1 > m2) or (h1 == h2 and m1 == m2): h2 += 24
    
    m1 += h1*60
    m2 += h2*60
    print(m2-m1)
