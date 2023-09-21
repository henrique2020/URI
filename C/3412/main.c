#include <stdio.h>

int main(void) {
    int p, e, n;
    int g, trocas = 0, t;
    scanf("%d %d %d", &p, &e, &n);

    g = p+e;
    while(g >= n){
        t = g/n;
        trocas += t;
        g = g%n + t;
    }

    printf("%d\n", trocas);
    return 0;
}
