//a, b, c = números 1, 2 e 3
#include <stdio.h>

int main() {
    double a, b, c;
    double triangulo, circulo, trapezio, quadrado, retangulo;
    double pi = 3.14159;
    scanf("%lf %lf %lf", &a, &b, &c);
    triangulo = (a*c)/2;
    printf("TRIANGULO: %.3lf\n", triangulo);

    circulo = pi*(c*c);
    printf("CIRCULO: %.3lf\n", circulo);

    trapezio = ((a+b)*c)/2;
    printf("TRAPEZIO: %.3lf\n", trapezio);

    quadrado = b*b;
    printf("QUADRADO: %.3lf\n", quadrado);

    retangulo = a*b;
    printf("RETANGULO: %.3lf\n", retangulo);
    return 0;
}
