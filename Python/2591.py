rep = int(input())
for _ in range(rep):
    poder = input().split('k')
    a = poder[0].count('a') * poder[1].count('a')
    print(f'k{"a"*a}')
