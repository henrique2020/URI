n1 = str(int(input()))
n2 = str(int(input()))
n3 = str(int(input()))

num_char = 10

print('A = {}, B = {}, C = {}'.format(n1, n2, n3))
print('A = {}, B = {}, C = {}'.format(n1.rjust(num_char), n2.rjust(num_char), n3.rjust(num_char)))
print('A = {}, B = {}, C = {}'.format(n1.zfill(num_char), n2.zfill(num_char), n3.zfill(num_char)))
print('A = {}, B = {}, C = {}'.format(n1.ljust(num_char), n2.ljust(num_char), n3.ljust(num_char)))
