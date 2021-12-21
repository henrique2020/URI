in_ = 0
out_ = 0

rep = int(input())
while(rep):
    num = int(input())
    if num >= 10 and num <= 20: in_ += 1
    else: out_ += 1
    rep -= 1

print("%d in" % in_)
print("%d out" % out_)
