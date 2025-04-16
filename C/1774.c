#include <stdio.h>
#include <stdlib.h>

typedef struct conexao{
    int r1;
    int r2;
    int custo;
} CONEXAO;

int comp(const void *a, const void *b){
    CONEXAO *v1 = (CONEXAO*)a, *v2 = (CONEXAO*)b;
    if(v1->custo > v2->custo) { return 1; }
    else if(v1->custo < v2->custo) { return -1; }
    return 0;
}

int main() {
    int roteadores, cabos, custoTotal = 0;
    scanf("%d %d", &roteadores, &cabos);

    CONEXAO conexoes[cabos];
    for(int i = 0; i < cabos; i++){
        int r1, r2, custo;
        scanf("%d %d %d", &r1, &r2, &custo);
        conexoes[i].r1 = r1;
        conexoes[i].r2 = r2;
        conexoes[i].custo = custo;
    }

    qsort(conexoes, cabos, sizeof(CONEXAO), comp);

    int custo[cabos+1];
    for(int i = 1; i <= roteadores; i++){
        custo[i] = i;
    }

    for(int i = 0; i < cabos; i++){
        int r1 = conexoes[i].r1,
            r2 = conexoes[i].r2;

        int corX = custo[r1],
            corY = custo[r2];

        if(corX == corY){
            continue;
        }
        custoTotal += conexoes[i].custo;

        for (int j = 1; j <= roteadores; j++){
            if(custo[j] == corX){
                custo[j] = corY;
            }
        }
    }

    printf("%d\n", custoTotal);

    return 0;
}
