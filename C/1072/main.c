//in e out = valores de saida do URI || rep = repetições || Intervalo -> 10-20
#include <stdio.h>

int main() {
    int rep, i, in, out, numero;
    in = 0;
    out = 0;
    i = 1;
    scanf("%d", &rep);

    while (i <= rep){
        scanf("%d", &numero);
        if(numero >= 10 && numero <= 20){
            in++;
        }
        else{
            out++;
        }
        i++;
    }
    printf("%d in\n", in);
    printf("%d out\n", out);
    return 0;
}
