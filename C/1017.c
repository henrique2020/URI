//Foi dado que o consumo do carro � de 12 KM/L
#include <stdio.h>

int main() {
    int tempo, velocidade;
    float gasolina;
    scanf("%d %d", &tempo, &velocidade);
    gasolina = (tempo*velocidade)/12.0; //12.0 para que d� como resultado um float
    printf("%.3f\n", gasolina);
    return 0;
}
