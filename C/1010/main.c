// cp, np, vp = c�digo da pe�a, o n�mero de pe�as e valor unit�rio da pe�a
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
