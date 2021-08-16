// cp, np, vp = código da peça, o número de peças e valor unitário da peça
#include <stdio.h>

int main() {
    int cp1, cp2, np1, np2;
    float vp1, vp2, valor;
    scanf("%d %d %f", &cp1, &np1, &vp1);
    scanf("%d %d %f", &cp2, &np2, &vp2);
    valor = (np1*vp1)+(np2*vp2);
    printf("VALOR A PAGAR: R$ %.2lf\n", valor);
    return 0;
}
