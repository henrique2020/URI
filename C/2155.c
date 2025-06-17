#include <stdio.h>
#include <math.h>
#include <string.h>

#define ICOSAEDROS 7
#define INF 999999999.99999

int melhorCaminho[ICOSAEDROS];
double melhorDistancia;

typedef struct Icosaedro {
    int estrelas;
    int x, y;
} ICOSAEDRO;

double distancia(ICOSAEDRO p1, ICOSAEDRO p2) {
    return sqrt(
        ((p1.x - p2.x) * (p1.x - p2.x)) +
        ((p1.y - p2.y) * (p1.y - p2.y))
    );
}

void tsp(int v, int niv, ICOSAEDRO *icos, int *caminho, int *visitados, int inicio) {
    caminho[niv] = v;

    if (niv == ICOSAEDROS-1) {
        double total = 0;
        for(int i = 0; i < ICOSAEDROS-1; i++) {
            total += distancia(icos[caminho[i]], icos[caminho[i + 1]]);
        }
        total += distancia(icos[caminho[ICOSAEDROS-1]], icos[caminho[0]]);

        if (total < melhorDistancia) {
            melhorDistancia = total;
            memcpy(melhorCaminho, caminho, ICOSAEDROS * sizeof(int));
        } else if (total == melhorDistancia) {
            int melhor = 0;
            for(int j = 0; j < ICOSAEDROS; j++) {
                int estrela_atual = icos[caminho[j]].estrelas;
                int estrela_melhor = icos[melhorCaminho[j]].estrelas;

                if (estrela_atual < estrela_melhor) {
                    melhor = 1;
                    break;
                } else if (estrela_atual > estrela_melhor) {
                    break;
                }
            }

            if (melhor) { memcpy(melhorCaminho, caminho, ICOSAEDROS * sizeof(int)); }
        }

        return;
    }

    for(int i = 1; i < ICOSAEDROS; i++) {
        if (visitados[i] == 0) {
            visitados[i] = 1;
            tsp(i, niv + 1, icos, caminho, visitados, inicio);
            visitados[i] = 0;   //Faz o backtrack (libera para o próximo caso de teste)
        }
    }
}

int main(){
    int rep;
    scanf("%d", &rep);

    for(int r = 1; r <= rep; r++) {
        ICOSAEDRO icos[ICOSAEDROS];
        int i = 0;
        int caminho[ICOSAEDROS], visitados[ICOSAEDROS];

        icos[i].estrelas = 4;
        scanf("%d %d", &icos[i].x, &icos[i].y);
        i++;

        for (i; i < ICOSAEDROS; i++) {
            scanf("%d %d %d", &icos[i].estrelas, &icos[i].x, &icos[i].y);
            visitados[i] = 0;
            caminho[i] = 0;
        }

        melhorDistancia = INF;
        visitados[0] = 1;
        tsp(0, 0, icos, caminho, visitados, 0);

        printf("Caso %d:\n", r);
        printf("4");
        for (i = 1; i < ICOSAEDROS; i++) {
            printf("->%d", icos[melhorCaminho[i]].estrelas);
        }
        printf("->4: %.5lf\n", melhorDistancia);
    }
    return 0;
}
