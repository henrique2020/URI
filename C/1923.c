#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CARACTERES 100

void bfs(int vi, int **G, int *nivel, int vertices) {
    int *fila = (int *)malloc(vertices * sizeof(int));
    int PA = 0, TD = 0;

    for (int i = 0; i < vertices; i++) nivel[i] = -1;

    fila[PA++] = vi;
    nivel[vi] = 0;

    while (PA != TD) {
        int v = fila[TD++];
        for (int j = 0; j < vertices; j++) {
            if (G[v][j] == 1 && nivel[j] == -1) {
                fila[PA++] = j;
                nivel[j] = nivel[v] + 1;
            }
        }
    }
    free(fila);
}

void ordena(char **convidados, int total_convidados){
    char aux[100];
    for(int i = 0; i < total_convidados; i++){
        for(int j = i; j < total_convidados; j++){
            if(strcasecmp(convidados[i], convidados[j]) > 0){
                strcpy(aux, convidados[j]);
                strcpy(convidados[j], convidados[i]);
                strcpy(convidados[i], aux);
            }
        }
    }
}

int busca_pos_nome(char **lista_nomes, char *nome, int range) {
    for (int i = 0; i < range; i++) {
        if (strcasecmp(lista_nomes[i], nome) == 0) {
            return i;
        }
    }
    return -1;
}

int main() {
    int relacoes, distancia_maxima, total_nomes = 0;
    scanf("%d %d", &relacoes, &distancia_maxima);

    int max_nomes = relacoes;

    char **nomes = (char **)malloc(max_nomes * sizeof(char *));
    for (int i = 0; i < max_nomes; i++) {
        nomes[i] = (char *)malloc(MAX_CARACTERES * sizeof(char));
    }

    int **iNome = (int **)malloc(max_nomes * sizeof(int *));
    for (int i = 0; i < max_nomes; i++) {
        iNome[i] = (int *)calloc(max_nomes, sizeof(int));
    }

    char n1[MAX_CARACTERES], n2[MAX_CARACTERES];
    for (int i = 0; i < relacoes; i++) {
        scanf("%s %s", n1, n2);

        int p1 = busca_pos_nome(nomes, n1, total_nomes);
        if (p1 == -1) {
            strcpy(nomes[total_nomes], n1);
            p1 = total_nomes++;
        }

        int p2 = busca_pos_nome(nomes, n2, total_nomes);
        if (p2 == -1) {
            strcpy(nomes[total_nomes], n2);
            p2 = total_nomes++;
        }

        iNome[p1][p2] = iNome[p2][p1] = 1;
    }


    int *nivel = (int *)malloc(total_nomes * sizeof(int));
    bfs(0, iNome, nivel, total_nomes);

    char **convidados = (char **)malloc(total_nomes * sizeof(char *));
    for (int i = 0; i < total_nomes; i++) {
        convidados[i] = (char *)malloc(MAX_CARACTERES * sizeof(char));
    }
    free(iNome);

    int total_convidados = 0;
    for (int i = 0; i < total_nomes; i++) {
        if(nivel[i] > 0 && nivel[i] <= distancia_maxima){
            strcpy(convidados[total_convidados++], nomes[i]);
        }
    }

    free(nivel);
    free(nomes);

    ordena(convidados, total_convidados);
    printf("%d\n", total_convidados);
    for (int i = 0; i < total_convidados; i++) {
        printf("%s\n", convidados[i]);
    }
    return 0;
}
