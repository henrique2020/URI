from math import gcd
rep = int(input())
while rep:
    R, V = map(int, input().split())
    print(gcd(R, V))
    rep-=1
