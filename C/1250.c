#include <stdio.h>

int main() {
    int rep, mov, ace, i, i2;
    scanf("%d", &rep);
    for(i = 0; i < rep; i++){
        ace = 0;
        scanf("%d", &mov);

        int tiro[mov];
        for(i2 = 0; i2 < mov; i2++){
            scanf("%d", &tiro[i2]);
        }

        char pulo[mov+1];
        scanf("%s", pulo);

        for(i2 = 0; i2 < mov; i2++){
            if((tiro[i2] <= 2 && pulo[i2] == 'S') || (tiro[i2] >= 3 && pulo[i2] == 'J')){
                ace++;
            }
        }
        printf("%d\n", ace);
    }
    return 0;
}
