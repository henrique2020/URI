#include <stdio.h>
#include <stdlib.h>

typedef struct nodo {
    int num;
    struct nodo *dir;
    struct nodo *esq;
} NODO;

NODO* insere(NODO* no, int numero) {
    if (no == NULL) {
        NODO* novo = (NODO*) malloc(sizeof(NODO));
        novo->num = numero;
        novo->esq = novo->dir = NULL;
        return novo;
    }

    if (numero < no->num)
        no->esq = insere(no->esq, numero);
    else
        no->dir = insere(no->dir, numero);

    return no;
}


void bfs(NODO *no, int n){
    NODO *fila[n];
    int PA = 0, TD = 0;
    fila[PA++] = no;

    while(PA != TD){
        NODO *nodo = fila[TD++];

        if(TD != 1)
            printf(" ");

        printf("%d", nodo->num);
        if(nodo->esq) fila[PA++] = nodo->esq;
        if(nodo->dir) fila[PA++] = nodo->dir;
    }
}

int main() {
    int casos, nos, numero;
    scanf("%d", &casos);
    for(int i = 0; i < casos; i++){
        int nos;
        scanf("%d", &nos);

        NODO *raiz = NULL;
        for(int j = 0; j < nos; j++){
            scanf("%d", &numero);
            raiz = insere(raiz, numero);
        }

        printf("Case %d:\n", i+1);
        bfs(raiz, nos);
        printf("\n\n");
    }
    return 0;
}
