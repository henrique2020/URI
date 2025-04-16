#include <stdio.h>

int main() {
    int distancia;
    float gasolina, media;
    scanf("%d %f", &distancia, &gasolina);
    media = distancia/gasolina;
    printf("%.3f km/l\n", media);
    return 0;
}
