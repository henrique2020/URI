//i, f = inicio e fim
#include <stdio.h>

int main() {
    int i, f, tempo;
    int dia = 24;
    scanf("%d %d", &i, &f);
    if(i == f){
        printf("O JOGO DUROU %d HORA(S)\n", dia);
    }
    else if(i > f){
        tempo = dia-(i-f);
        printf("O JOGO DUROU %d HORA(S)\n", tempo);
    }
    else{
        tempo = f-i;
        printf("O JOGO DUROU %d HORA(S)\n", tempo);
    }
    return 0;
}
