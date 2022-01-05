arr = []
arr.append(int(input()))
arr.append(int(input()))
arr.sort()
for x in range(arr[0]+1, arr[1]):
    if x%5 == 2 or  x%5 == 3:
        print(x)
