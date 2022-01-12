rep = int(input())
numbers = []
numbers_list = {''}
numbers_list.remove('')
while rep:
    n = int(input())
    numbers.append(n)
    numbers_list.add(n)
    rep-=1

values = sorted(numbers_list)
for count in values:
    print('{} aparece {} vez(es)'.format(count, numbers.count(count)))
