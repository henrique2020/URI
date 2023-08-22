#include <stdio.h>
#include <string.h>

int main(){
    int rep, i, j, cod;
    int len = 100;   //Valor máximo pré-definido = 50
    char frase[len], cifra[len];
    scanf("%d", &rep);
    for(i = 0; i<rep; i++){
        getchar();
        fgets(frase, len, stdin);
        frase[strlen(frase)-1] = '\0';
        scanf("%d", &cod);

        for(j = 0; frase[j] != '\0'; j++){
            int pos = frase[j] - cod;
            if(pos >= 'A'){ cifra[j] = pos; }
            else{ cifra[j] = pos+('Z'-'A'+1); }
        }
        cifra[j] = '\0';
        printf("%s\n", cifra);
    }
    return 0;
}
