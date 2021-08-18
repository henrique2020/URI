//rep, mov, ace = repetições, movimentos, vezes que ele é atingido
#include <stdio.h>

int main() {
    int rep, mov, ace, i;
    i = 0;
    scanf("%d", &rep);
    while(i < rep){
        ace = 0;
        int i2;
        scanf("%d", &mov);

        int tiro[mov];
        for(i2 = 0; i2 < mov; i2++){
            scanf("%d", &tiro[i2]);
        }

        char pulo[mov];
        scanf("%s", &pulo);

        for(i2 = 0; i2 < mov; i2++){
            if((tiro[i2] <= 2 && pulo[i2] == 'S') || (tiro[i2] > 2 && pulo[i2] == 'J')){
                ace++;
            }
        }
        printf("%d\n", ace);
        i+= 1;
    }
    return 0;
}
