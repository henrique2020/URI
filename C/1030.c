#include <stdio.h>
#include <stdlib.h>

typedef struct nodo {
    int valor;
    struct nodo *ant;
    struct nodo *prox;
} NODO;

NODO *criaNo(int num) {
    NODO *novo = (NODO *) malloc(sizeof(NODO));
    novo->valor = num;
    novo->ant = NULL;
    novo->prox = NULL;
    return novo;
}

int main() {
    int rep, pessoas, saltos;
    scanf("%d", &rep);
    for(int i = 1; i <= rep; i++){
        scanf("%d %d", &pessoas, &saltos);

        NODO *pessoa = criaNo(1);
        NODO *primeiro = pessoa;
        for (int j = 2; j <= pessoas; j++){
            pessoa->prox = criaNo(j);
            pessoa->prox->ant = pessoa;
            pessoa = pessoa->prox;

            if (j == pessoas) {
                primeiro->ant = pessoa;
                pessoa->prox = primeiro;
            }
        }

        while(pessoa->prox != pessoa){
            for(int j = 0; j < saltos; j++){
                pessoa = pessoa->prox;
            }

            pessoa->ant->prox = pessoa->prox;
            pessoa->prox->ant = pessoa->ant;

            pessoa = pessoa->ant;
        }

        printf("Case %d: %d\n", i, pessoa->valor);

    }
    return 0;
}
