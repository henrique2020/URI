#include <stdio.h>
#include <math.h>

int main(){
    int rep, gols;
    int r, g, b, maior_placar;
    r =  g = b = maior_placar = 0;
    scanf("%d", &rep);

    for(int i; i < rep; i++){
        scanf("%d", &gols);

        char t1, t2;
        for(int j = 0; j < gols; j++){
            getchar();
            scanf("%c %c", &t1, &t2);

            if(t1 == 'R') {
                if(t2 == 'G')
                    r += 2;
                else if(t2 == 'B')
                    r += 1;

                if(r > maior_placar)
                    maior_placar = r;
            }

            else if(t1 == 'G') {
                if(t2 == 'B')
                    g += 2;
                else if(t2 == 'R')
                    g += 1;

                if(g > maior_placar)
                    maior_placar = g;
            }

            else if(t1 == 'B') {
                if(t2 == 'R')
                    b += 2;
                else if(t2 == 'G')
                    b += 1;

                if(b > maior_placar)
                    maior_placar = b;
            }
        }

        if(r == g && g == b)
            printf("trempate\n");

        else if(
           (r == maior_placar && g == maior_placar)
           || (g == maior_placar && b == maior_placar)
           || (b == maior_placar && r == maior_placar)
        )
            printf("empate\n");

        else {
            if(r == maior_placar)
                printf("red\n");
            else if(g == maior_placar)
                printf("green\n");
            else if(b == maior_placar)
                printf("blue\n");
        }
    }

    return 0;
}
