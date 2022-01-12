## Caso de teste 1
while True:
    ini, fim = map(int, input().split())
    if (ini == 0 and fim == 0):
        break

    count = {
        '0':0,
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0
        }
        
    for x in range(ini, fim+1):
        num = list(map(str, str(x)))
        for c in num:
            count[c]+=1
    
    print('%d %d %d %d %d %d %d %d %d %d' % (count['0'], count['1'], count['2'], count['3'], count['4'], count['5'], count['6'], count['7'], count['8'], count['9']))
    
    
    
## Caso de teste 2
while True:
    ini, fim = map(int, input().split())
    if (ini == 0 and fim == 0):
        break

    count = [0,0,0,0,0,0,0,0,0,0]  
    for x in range(ini, fim+1):
        num = list(map(str, str(x)))
        for c in num:
            count[int(c)]+=1
    
    print('%d %d %d %d %d %d %d %d %d %d' % (count[0], count[1], count[2], count[3], count[4], count[5], count[6], count[7], count[8], count[9]))

    
    
## Caso de teste 3
while True:
    ini, fim = map(int, input().split())
    if (ini == 0 and fim == 0):
        break

    num = []
    for x in range(ini, fim+1):
        num += list(map(int, str(x)))

    print('%d %d %d %d %d %d %d %d %d %d' % (num.count(0), num.count(1), num.count(2), num.count(3), num.count(4), num.count(5), num.count(6), num.count(7), num.count(8), num.count(9)))

    
## Resolução do Giuliano, funciona!
while True:

    value = input().split()

    first, last = int(value[0]), int(value[1])

    if (first == 0 and last == 0) :
        break

    all_cases = []
    all_cases_last = []


    def format_number(x, y):
        original_value = x
        exp = 0
        rest = 0
        
        while x/10 >= 1:
            exp += 1
            x = int(x/10)
        rest = x
        if y:
            all_cases.append([exp, rest, (original_value - (10**exp)*rest)])
            if ((original_value - (10**exp)*rest) != 0):
                format_number(original_value - (10**exp)*rest, y)
        
        else:
            all_cases_last.append([exp, rest, (original_value - (10**exp)*rest)])
            if ((original_value - (10**exp)*rest) != 0):
                format_number(original_value - (10**exp)*rest, y)

    def check_case(a, k, b, i):
        if a < i:
            soma = a*k*(10**(k-1))
        elif a == i:
            soma = a*k*(10**(k-1)) + 1 + b
        elif a > i:
            soma = (a*k + 10)*(10**(k-1))
        return int(soma)

    def calc_T_n(k, b, a):
        constante = (k + 1)*(b + 1 + (a - 1) * (10**k))
        somatorio = 0

        for number in range(1, (k+1)):
            somatorio += 9*number*(10**(number-1))

        return constante + somatorio
        

    format_number(first-1, True)
    format_number(last, False)

    amount_first = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    amount_last = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for data in all_cases:
        amount_first[1] += check_case(data[1], data[0], data[2], 1)
        amount_first[2] += check_case(data[1], data[0], data[2], 2)
        amount_first[3] += check_case(data[1], data[0], data[2], 3)
        amount_first[4] += check_case(data[1], data[0], data[2], 4)
        amount_first[5] += check_case(data[1], data[0], data[2], 5)
        amount_first[6] += check_case(data[1], data[0], data[2], 6)
        amount_first[7] += check_case(data[1], data[0], data[2], 7)
        amount_first[8] += check_case(data[1], data[0], data[2], 8)
        amount_first[9] += check_case(data[1], data[0], data[2], 9)
        
    amount_first[0] = calc_T_n(all_cases[0][0], all_cases[0][2], all_cases[0][1]) - sum(amount_first)



    for data in all_cases_last:
        amount_last[1] += check_case(data[1], data[0], data[2], 1)
        amount_last[2] += check_case(data[1], data[0], data[2], 2)
        amount_last[3] += check_case(data[1], data[0], data[2], 3)
        amount_last[4] += check_case(data[1], data[0], data[2], 4)
        amount_last[5] += check_case(data[1], data[0], data[2], 5)
        amount_last[6] += check_case(data[1], data[0], data[2], 6)
        amount_last[7] += check_case(data[1], data[0], data[2], 7)
        amount_last[8] += check_case(data[1], data[0], data[2], 8)
        amount_last[9] += check_case(data[1], data[0], data[2], 9)
        
    amount_last[0] = calc_T_n(all_cases_last[0][0], all_cases_last[0][2], all_cases_last[0][1]) - sum(amount_last)

    cont = 0

    final_vector = [0,0,0,0,0,0,0,0,0,0]

    while cont < 10:
        final_vector[cont] = amount_last[cont] - amount_first[cont]
        cont +=1

    print(final_vector[0], final_vector[1], final_vector[2], final_vector[3], final_vector[4], final_vector[5], final_vector[6], final_vector[7], final_vector[8], final_vector[9])
