//n100, n50, n20, n10, n5, n2, n1 = nota de R$ 100, 50, 20, 10, 5, 2 e 1
#include <stdio.h>

int main() {
    int dinheiro, n100, n50, n20, n10, n5, n2, n1;
    scanf("%d", &dinheiro);
    printf("%d\n", dinheiro);

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
    n1 = dinheiro;

    printf("%d nota(s) de R$ 100,00\n", n100);
    printf("%d nota(s) de R$ 50,00\n", n50);
    printf("%d nota(s) de R$ 20,00\n", n20);
    printf("%d nota(s) de R$ 10,00\n", n10);
    printf("%d nota(s) de R$ 5,00\n", n5);
    printf("%d nota(s) de R$ 2,00\n", n2);
    printf("%d nota(s) de R$ 1,00\n", n1);
    return 0;
}
