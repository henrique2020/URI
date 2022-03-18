#include<stdio.h>

int main(){
    int tam, i, j;
    for(;;){   //Laço de repetição infinita = while(1) -> while(true)
        scanf("%d", &tam);
        if(tam == 0){   //Condição de encerramento do loop
            break;
        }
        for(i = 1; i <= tam; i++){
            for(j = 1; j <= tam; j++){
                if(i <= j){
                   printf("%3d", 1+(j-i));
                }
                else{
                    printf("%3d", 1+(i-j));
                }
                
                if (j < tam){
                    printf(" ");
                }
                
            }
            printf("\n");
        }
        printf("\n");
    }
    
    return 0;
}