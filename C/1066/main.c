//'rep' é um valor pré-definido na questão
#include <stdio.h>

int main() {
    int rep, valor, i;
    int par, impar, positivo, negativo;
    rep = 5;
    par = 0;
    impar = 0;
    positivo = 0;
    negativo = 0;
    for (i = 0; i < rep; i++){
        scanf("%d", &valor);
        if(valor > 0){
            positivo++;
            if (valor % 2 == 0){
                par++;
            }
            else{
                impar++;
            }
        }
        else if(valor < 0){
            negativo++;
            if (valor % 2 == 0){
                par++;
            }
            else{
                impar++;
            }
        }
        else{
            par++;
        }
    }
    printf("%d valor(es) par(es)\n", par);
    printf("%d valor(es) impar(es)\n", impar);
    printf("%d valor(es) positivo(s)\n", positivo);
    printf("%d valor(es) negativo(s)\n", negativo);
    return 0;
}
