for x in range(int(input())):
    number = input()
    if len(number) == 3:
        if ('tw' in number or 'wo' in number or ('t' == number[0] and 'o' == number[2])):
            print('2')
        else:
            print('1')
    else:
        print('3')
