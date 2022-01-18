d1, d2, d3 = map(int, input().split())

if d1 > d2 and d3 >= d2:
    print(':)')
elif d2 > d1 and d3 > d2 and (d3-d2) >= (d2-d1):
    print(':)')
elif d1 > d2 and d2 > d3 and (d1-d2) > (d2-d3):
    print(':)')
elif d2 == d1 and d3 > d2:
    print(':)')
else:
    print(':(')
