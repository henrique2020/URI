//Versão montada apenas para usar no URI
//Codigo não faz uso de matriz!!!
#include<stdio.h>

int main(){
    int tam = 12, line, i, j;    //Valor pré-definido na questão
    float soma;
    char op[2];    
    scanf("%d", &line); //vai ser sempre entre 0 e 11 
    scanf("%s", &op[0]);    //Vai ser sempre 1 letra maiúscula (S ou M)
    
    soma = 0.0;
    for(i = 0; i < tam; i++){
        for(j = 0; j < tam; j++){
            float temp;
            scanf("%f", &temp);
            if(i == line){
                soma+=temp;
            }
        }
    }
    
    if(op[0] == 'M'){
        soma /= tam;
    }
    
    printf("%.1f\n", soma);
    
    return 0;
}