//r = raio || pi já definido -> 3.14159
#include <stdio.h>
#include <math.h>

int main() {
    double r, volume;
    double pi = 3.14159;
    scanf("%lf", &r);
    volume = (4.0/3)*pi*pow(r, 3); //Caso coloque 4/3, ele considera como um resultado 'int', o que causa erro
    printf("VOLUME = %.3lf\n", volume);
    return 0;
}
