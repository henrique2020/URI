// n, h, v = número, horas trabalhadas e valor por hora
#include <stdio.h>

int main() {
    int n, h;
    float v, salario;
    scanf("%d %d %f", &n, &h, &v);
    salario = h*v;
    printf("NUMBER = %d\n", n);
    printf("SALARY = U$ %.2f\n", salario);
    return 0;
}
