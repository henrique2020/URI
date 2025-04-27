#include <stdio.h>

#define MAX 50
int grafo[MAX][MAX];
int nivel[MAX];
int low[MAX];
int pontes;

void dfs(int v, int niv, int N) {
    nivel[v] = niv;

    for (int i = 0; i < N; i++) {
        if (grafo[v][i] == 1 && nivel[i] == -1) {
            grafo[v][i] = 2;     // Aresta de árvore
            grafo[i][v] = 0;     // Remove a direção contrária
            dfs(i, niv + 1, N);
        }
    }
}

int lowpt(int v, int N) {
    if (low[v] != -1)
        return low[v];  // Se já foi calculado, retorna

    low[v] = v; // Inicializa com o próprio vértice

    for (int i = 0; i < N; i++) {
        if (grafo[v][i] == 2) {
            int low_i = lowpt(i, N);
            if (nivel[low_i] < nivel[low[v]])
                low[v] = low_i; // Atualiza se encontrou valor menor
        } else if (grafo[v][i] == 1 && nivel[i] < nivel[low[v]]) {
            low[v] = i; // Aresta de retorno para antecessor
        }
    }

    // Verifica se é uma ponte: low[filho] > nivel[pai]
    for (int i = 0; i < N; i++) {
        if (grafo[v][i] == 2) {
            if (nivel[low[i]] > nivel[v])
                pontes++;
        }
    }

    return low[v];
}

int main() {
    int cidades, conexoes;
    while (scanf("%d %d", &cidades, &conexoes) != EOF) {
        
        for (int i = 0; i < cidades; i++) {
            for (int j = 0; j < cidades; j++)
                grafo[i][j] = 0;
            nivel[i] = -1;
            low[i] = -1;
        }

        for (int i = 0; i < conexoes; i++) {
            int c1, c2;
            scanf("%d %d", &c1, &c2);
            c1--; c2--;
            grafo[c1][c2] = 1;
            grafo[c2][c1] = 1;
        }

        dfs(0, 0, cidades);

        pontes = 0;
        for (int i = 0; i < cidades; i++) {
            lowpt(i, cidades);
        }

        printf("%d\n", pontes);
    }

    return 0;
}