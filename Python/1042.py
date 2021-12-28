arr = input().split()
arr_sort = sorted(arr, key=int)

for pos in arr_sort:
    print(pos)

print()

for pos in arr:
    print(pos)
