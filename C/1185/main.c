//Versão montada apenas para usar no URI
//Codigo não faz uso de matriz!!!
#include<stdio.h>

int main(){
    int tam = 12, i, j, n;    //Valor pré-definido na questão
    float mat[tam][tam], soma;
    char op[1];
    
    scanf("%s", &op[0]);    //Vai ser sempre 1 letra maiúscula (S ou M)
    
    soma = 0.0;
    for(i = 0; i < tam; i++){
        for(j = tam-1; j >= 0; j--){
            float temp;
            scanf("%f", &temp);
            if(i < j){
                soma+=temp;
            }
        }
    }

    if(op[0] == 'M'){
        int n = ((tam*tam)-tam)/2;
        soma /= n;
    }

    printf("%.1f\n", soma);

    return 0;
}