while 1:
    entrada = input()
    if entrada[0] == '-':
        break

    else:
        if (len(entrada) >= 3 and entrada[1] == 'x'):
            value = str(int(entrada, 16))
        else:
            value = str(hex(int(entrada)))
            value = str(value[0:2])+str(value[2:]).upper()
        print(f'{value}')
