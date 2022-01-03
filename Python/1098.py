i = 0.0
while i <= 2:
    if round(i, 1)%1 == 0:
        print('I=%.0f J=%.0f' % (i, 1+i))
        print('I=%.0f J=%.0f' % (i, 2+i))
        print('I=%.0f J=%.0f' % (i, 3+i))
    else:
        print('I=%.1f J=%.1f' % (i, 1+i))
        print('I=%.1f J=%.1f' % (i, 2+i))
        print('I=%.1f J=%.1f' % (i, 3+i))
    i+=0.2
