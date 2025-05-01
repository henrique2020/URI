#include <stdio.h>
#include <string.h>

#define MAX 400
int grafo[MAX][MAX];
int nivel[MAX];
int low[MAX];
int pai[MAX];
int articulacao[MAX]; // 1 se for articulação

void dfs(int v, int niv, int N) {
    nivel[v] = low[v] = niv;
    int filhos = 0;

    for (int i = 0; i < N; i++) {
        if (grafo[v][i] == 1) {
            if (nivel[i] == -1) {
                pai[i] = v;
                filhos++;
                dfs(i, niv + 1, N);

                if (low[i] < low[v])
                    low[v] = low[i];

                if (pai[v] != -1 && low[i] >= nivel[v])
                    articulacao[v] = 1;

            } else if (i != pai[v]) {
                if (nivel[i] < low[v])
                    low[v] = nivel[i];
            }
        }
    }

    // Se v é a raiz e tem 2 ou mais filhos, é articulação
    if (pai[v] == -1 && filhos > 1)
        articulacao[v] = 1;
}

int main() {
    int computadores, conexoes, teste = 1;

    while (1) {
        scanf("%d %d", &computadores, &conexoes);
        if (computadores == 0 && conexoes == 0)
            break;

        memset(grafo, 0, sizeof(grafo));
        for (int i = 0; i < computadores; i++) {
            nivel[i] = -1;
            low[i] = -1;
            pai[i] = -1;
            articulacao[i] = 0;
        }

        for (int i = 0; i < conexoes; i++) {
            int c1, c2;
            scanf("%d %d", &c1, &c2);
            c1--; c2--;
            grafo[c1][c2] = 1;
            grafo[c2][c1] = 1;
        }

        dfs(0, 0, computadores);
        printf("Teste %d\n", teste++);
        int encontrou = 0;
        int primeiro = 1;
        for (int i = 0; i < computadores; i++) {
            if (articulacao[i]) {
                printf("%d ", i + 1);
                encontrou = 1;
            }
        }

        if (!encontrou)
            printf("nenhum");

        printf("\n\n");
    }

    return 0;
}