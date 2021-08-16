// n, s, v = nome, salário fixo e vendas efetuadas (em dinheiro)
#include <stdio.h>

int main() {
    char n[20];
    double s, v, salario;
    scanf("%s %lf %lf", &n, &s, &v);
    salario = s+(v*0.15);
    printf("TOTAL = R$ %.2lf\n", salario);
    return 0;
}
