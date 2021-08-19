#include <stdio.h>
#include <stdlib.h>

int ascending(void const *a, void const *b )
{
    return (*(int*)a - *(int*)b );
}

int descending(void const *a, void const *b )
{
    return (*(int*)b - *(int*)a );
}

int main() {
    int tamanho, par, impar;
    par = 0;
    impar = 0;
    scanf("%d", &tamanho);
    int numeros[tamanho];
    int pares[tamanho], impares[tamanho];
    int i = 0;
    for(i = 0; i < tamanho; i++){
        int numero;
        scanf("%d", &numero);
        if(numero%2 == 0){
            pares[par] = numero;
            par++;
        }
        else{
            impares[impar] = numero;
            impar++;
        }
    }

    qsort(pares, par, sizeof(int), ascending);
    qsort(impares, impar, sizeof(int), descending);

    for(i = 0; i < par; i++){
        printf("%d\n", pares[i]);
    }
    for(i = 0; i < impar; i++){
        printf("%d\n", impares[i]);
    }
    return 0;
}
