pecas = int(input())
min_l, max_l = map(int, input().split())
min_s, max_s = map(int, input().split())

if ((min_l <= pecas <= max_l) and (min_s <= pecas <= max_s)):
    print("possivel")
else:
    print("impossivel")
