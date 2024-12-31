rep = int(input())
for _ in range(rep):
    n_min, n_max = map(int, input().split())
    string = ''.join(map(str, range(n_min, n_max + 1)))
    print(string, string[::-1], sep='')
