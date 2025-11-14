// Problema: 1976 - Matrizes | Resposta: Accepted
// Linguagem: C99 [+0s]      | Tempo: 1.844s

#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

#define MAX 1001

long long custo_minimo[MAX][MAX];
int ponto_de_corte[MAX][MAX];
int dimensao[MAX];

void imprimeOrdem(int i, int j) {
    if (i == j) {
        printf("A%d", i);
        return;
    }
    printf("(");
    imprimeOrdem(i, ponto_de_corte[i][j]);
    imprimeOrdem(ponto_de_corte[i][j] + 1, j);
    printf(")");
}

int main() {
    int N;
    while (scanf("%d", &N) == 1 && N != 0) {
        for (int i = 1; i <= N; i++) {
            int L, C;
            scanf("%d %d", &L, &C);
            if (i == 1) dimensao[0] = L;
            dimensao[i] = C;
        }

        for (int i = 1; i <= N; i++)
            custo_minimo[i][i] = 0;

        // calcula cadeias de tamanho 2 até N
        for (int tam = 2; tam <= N; tam++) {
            for (int i = 1; i <= N - tam + 1; i++) {
                int j = i + tam - 1;
                custo_minimo[i][j] = LLONG_MAX;
                for (int k = i; k < j; k++) {
                    long long custo = 
                        custo_minimo[i][k] 
                        + custo_minimo[k + 1][j]
                        + (long long)dimensao[i - 1] * dimensao[k] * dimensao[j];
                    if (custo < custo_minimo[i][j]) {
                        custo_minimo[i][j] = custo;
                        ponto_de_corte[i][j] = k;
                    }
                }
            }
        }

        int temEmpate = 0;
        for (int i = 1; i < N && !temEmpate; i++) {
            for (int j = i + 1; j <= N && !temEmpate; j++) {
                long long melhor = custo_minimo[i][j];
                int cont = 0;
                for (int k = i; k < j; k++) {
                    long long custo = 
                        custo_minimo[i][k] 
                        + custo_minimo[k + 1][j] 
                        + (long long) dimensao[i - 1] * dimensao[k] * dimensao[j];
                    if (custo == melhor) cont++;
                }
                if (cont > 1) temEmpate = 1;
            }
        }

        if (temEmpate)
            printf("%lld\n", custo_minimo[1][N]);
        else {
            imprimeOrdem(1, N);
            printf("\n");
        }
    }
    return 0;
}
