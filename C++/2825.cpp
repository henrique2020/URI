// Problema: 2825 - L de Atreus!? | Resposta: Accepted
// Linguagem: C++20 [+0s]         | Tempo: 2.241s

#include <stdio.h>
#include <string.h>

#define MAX_PALAVRA 100
#define MAX_DIC 1000

int minimum(int a, int b, int c) {
    if (a <= b && a <= c) return a;
    if (b <= c) return b;
    return c;
}

int LevenshteinDistance(char s[], char t[]) {
    int d[MAX_PALAVRA + 1][MAX_PALAVRA + 1];
    int m = strlen(s);
    int n = strlen(t);
    int i, j;

    for (i = 0; i <= m; i++) d[i][0] = i;
    for (j = 0; j <= n; j++) d[0][j] = j;

    for (j = 1; j <= n; j++)
        for (i = 1; i <= m; i++)
            if (s[i - 1] == t[j - 1])
                d[i][j] = d[i - 1][j - 1];
            else
                d[i][j] = minimum(
                    d[i - 1][j] + 1,
                    d[i][j - 1] + 1,
                    d[i - 1][j - 1] + 1
                );

    return d[m][n];
}

char dicionario[MAX_DIC][MAX_PALAVRA + 1], corrigir[MAX_DIC][MAX_PALAVRA + 1];

int main() {
    int dic, cor;

    if (scanf("%d", &dic) != 1 || dic <= 0) return 0;
    for (int i = 0; i < dic; i++)
        scanf("%100s", dicionario[i]);

    if (scanf("%d", &cor) != 1 || cor <= 0) return 0;
    for (int i = 0; i < cor; i++)
        scanf("%100s", corrigir[i]);

    for (int i = 0; i < cor; i++) {
        char *temp = dicionario[0];
        int similaridade = 101;

        for (int j = 0; j < dic; j++) {
            int p = LevenshteinDistance(corrigir[i], dicionario[j]);
            if (p < similaridade) {
                similaridade = p;
                temp = dicionario[j];
                if (p == 0) break;
            }
        }

        if (i > 0) printf(" ");
        printf("%s", temp);
    }

    printf("\n");
    return 0;
}
