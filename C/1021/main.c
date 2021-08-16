//n100, n50, n20, n10, n5, n2 = notas de R$ 100.00, 50.00, 20.00, 10.00, 5.00 e 2.00 || m100, m50, m25, m10, m5 = moedas de R$ 1.00, 0.50, 0.25, 0.10, 0.05 || O que sobra de dinheiro são moedas de  R$ 0.01
#include <stdio.h>

int main() {
    float dinheiro;
    scanf("%f", &dinheiro);

    int n100, n50, n20, n10, n5, n2;
    n100 = dinheiro/100;
    dinheiro = dinheiro-(n100*100);
    n50 = dinheiro/50;
    dinheiro = dinheiro-(n50*50);
    n20 = dinheiro/20;
    dinheiro = dinheiro-(n20*20);
    n10 = dinheiro/10;
    dinheiro = dinheiro-(n10*10);
    n5 = dinheiro/5;
    dinheiro = dinheiro-(n5*5);
    n2 = dinheiro/2;
    dinheiro = dinheiro-(n2*2);

    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n", n100);
    printf("%d nota(s) de R$ 50.00\n", n50);
    printf("%d nota(s) de R$ 20.00\n", n20);
    printf("%d nota(s) de R$ 10.00\n", n10);
    printf("%d nota(s) de R$ 5.00\n", n5);
    printf("%d nota(s) de R$ 2.00\n", n2);

    int m100, m50, m25, m10, m5, m1;
    m100 = dinheiro;
    dinheiro = dinheiro-m100;
    m50 = dinheiro/0.5;
    dinheiro = dinheiro-(m50*0.5);
    m25 = dinheiro/0.25;
    dinheiro = dinheiro-(m25*0.25);
    m10 = dinheiro/0.1;
    dinheiro = dinheiro-(m10*0.1);
    m5 = dinheiro/0.05;
    dinheiro = dinheiro-(m5*0.05);
    dinheiro = dinheiro*100; // Dinheiro se torna o valor correspondente a moedas de 1 centavo

    printf("MOEDAS:\n");
    printf("%d moeda(s) de R$ 1.00\n", m100);
    printf("%d moeda(s) de R$ 0.50\n", m50);
    printf("%d moeda(s) de R$ 0.25\n", m25);
    printf("%d moeda(s) de R$ 0.10\n", m10);
    printf("%d moeda(s) de R$ 0.05\n", m5);
    printf("%.0f moeda(s) de R$ 0.01\n", dinheiro);
    return 0;
}
