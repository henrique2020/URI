#include <stdio.h>
#include <math.h>

#define PI 3.1415

double volume(int raio){
    return (4.0 / 3.0) * PI * pow(raio, 3);
}

int main(){
    int raio, gas;
    scanf("%d %d", &raio, &gas);

    int baloes = floor(gas / volume(raio));
    printf("%d\n", baloes);
    return 0;
}
