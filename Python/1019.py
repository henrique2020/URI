tempo = int(input())
h = tempo/3600;
m = (tempo%3600)/60;
s = (tempo%3600)%60;
print("%d:%d:%d" % (h, m, s));
