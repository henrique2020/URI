#include <stdio.h>

int main() {
    int rep, valor, i;
    scanf("%d", &rep);
    for (i = 0; i < rep; i++){
        scanf("%d", &valor);
        if(valor > 0){
            if (valor % 2 == 0){
                printf("EVEN POSITIVE\n");
            }
            else{
                printf("ODD POSITIVE\n");
            }
        }
        else if(valor < 0){
            if (valor % 2 == 0){
                printf("EVEN NEGATIVE\n");
            }
            else{
                printf("ODD NEGATIVE\n");
            }
        }
        else{
            printf("NULL\n");
        }
    }
    ;
    return 0;
}
