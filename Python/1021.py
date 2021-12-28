dinheiro = float(input())

n100 = dinheiro/100
n50 = (dinheiro%100)/50
n20 = ((dinheiro%100)%50)/20
n10 = (((dinheiro%100)%50)%20)/10
n5 = ((((dinheiro%100)%50)%20)%10)/5
n2 = (((((dinheiro%100)%50)%20)%10)%5)/2

m1 = ((((((dinheiro%100)%50)%20)%10)%5)%2)/1
m05 = (((((((dinheiro%100)%50)%20)%10)%5)%2)%1)/0.5
m025 = (((((((dinheiro%100)%50)%20)%10)%5)%2)%0.5)/0.25
m01 = ((((((((dinheiro%100)%50)%20)%10)%5)%2)%0.5)%0.25)/0.1
m005 = (((((((((dinheiro%100)%50)%20)%10)%5)%2)%0.5)%0.25)%0.1)/0.05
m001 = ((((((((((dinheiro%100)%50)%20)%10)%5)%2)%0.5)%0.25)%0.1)%0.05)/0.01

#print(n100,"---",n50,"---",n20,"---",n10,"---",n5,"---",n2)
#print(m1,"---",m05,"---",m025,"---",m01,"---",m005,"---",m001)

print("NOTAS:")
print("%d nota(s) de R$ 100.00" %n100)
print("%d nota(s) de R$ 50.00" %n50)
print("%d nota(s) de R$ 20.00" %n20)
print("%d nota(s) de R$ 10.00" %n10)
print("%d nota(s) de R$ 5.00" %n5)
print("%d nota(s) de R$ 2.00" %n2)

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %m1)
print("%d moeda(s) de R$ 0.50" %m05)
print("%d moeda(s) de R$ 0.25" %m025)
print("%d moeda(s) de R$ 0.10" %m01)
print("%d moeda(s) de R$ 0.05" %m005)
print("%d moeda(s) de R$ 0.01" %(m001+0.01))
