// Problema: 2825 - L de Atreus!? | Resposta: Accepted
// Linguagem: C99 [+0s]           | Tempo: 4.014s

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define PALAVRAS 1000
#define CARACTERES 101

int minimum(int a, int b, int c){
   if (a<=b && a<=c) return a;
   if (b<=c) return b;
   return c;
}

int LevenshteinDistance (char s [],char t []){
    // d is a table with m+1 rows and n+1 columns
    int d[CARACTERES + 1][CARACTERES + 1];
    int m=strlen(s);
    int n=strlen(t);
    int i,j;
    for (i=0;i<=m;i++) { d[i][0] = i; } // deletion
    for (j=0;j<=n;j++) { d[0][j] = j; } // insertion
    for (j=1;j<=n;j++)
       for (i=1;i<=m;i++)
          if (s[i-1] == t[j-1]) { d[i][j] = d[i-1][j-1]; }
          else
            d[i][j] = minimum (
                d[i -1][j] + 1, // deletion
                d[i][j-1] + 1, // insertion
                d[i-1][j-1] + 1 // substitution
            );

    return d[m][n];
}

int main() {
    char dicionario [PALAVRAS][CARACTERES], corrigir[PALAVRAS][CARACTERES];
    int dic, cor;

    scanf("%d", &dic);
    for(int i = 0; i < dic; i++)
        scanf("%s", dicionario[i]);


    scanf("%d", &cor);
    for(int i = 0; i < cor; i++)
        scanf("%s", corrigir[i]);

    for(int i = 0; i < cor; i++) {
        char *temp;
        int similaridade = 101;

        for(int j = 0; j < dic; j++) {

            int p = LevenshteinDistance(corrigir[i], dicionario[j]);
            if(p < similaridade) {
                similaridade = p;
                temp = dicionario[j];
                if(p == 0)
                    break;
            }
        }

        if(i == 0)
            printf("%s", temp);
        else
            printf(" %s", temp);
    }

    printf("\n");

    return 0;
}
