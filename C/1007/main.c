// a, b, c, d = número 1, 2, 3 e 4
#include <stdio.h>

int main() {
    int a, b, c, d, diferenca;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    diferenca = (a*b-c*d);
    printf("DIFERENCA = %d\n", diferenca);
    return 0;
}
