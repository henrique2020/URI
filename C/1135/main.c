#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

    while(1){
        int formigueiros;
        scanf("%d", &formigueiros);

        if(formigueiros == 0)
            break;

        int pai[formigueiros];
        int nivel[formigueiros];
        int distancia_pai[formigueiros];

        memset(pai, 0, sizeof(pai));
        memset(nivel, 0, sizeof(nivel));
        memset(distancia_pai, 0, sizeof(distancia_pai));

        for(int i = 1; i < formigueiros; i++){
            int p, f;
            scanf("%d %d", &p, &f);
            pai[i] = p;
            nivel[i] = nivel[p] + 1;
            distancia_pai[i] = f;
        }

        int consultas;
        scanf("%d", &consultas);

        long long int distancias[consultas];
        for(int i = 0; i < consultas; i++){
            int f1, f2;
            scanf("%d %d", &f1, &f2);

            long long int distancia = 0;
            while(f1 != f2){
                if(nivel[f1] > nivel[f2]){
                    distancia += distancia_pai[f1];
                    f1 = pai[f1];
                } else if(nivel[f1] < nivel[f2]){
                    distancia += distancia_pai[f2];
                    f2 = pai[f2];
                } else {
                    distancia += distancia_pai[f1] + distancia_pai[f2];
                    f1 = pai[f1];
                    f2 = pai[f2];
                }
            }

            distancias[i] = distancia;
        }

        for(int i = 0; i < consultas; i++){
            printf("%lld", distancias[i]);
            if(i+1 < consultas)
                printf(" ");
        }
        printf("\n");
    }

    return 0;
}
