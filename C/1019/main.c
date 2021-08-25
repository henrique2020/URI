//h, m, s = hora (3600s), minuto (60s) e segundo
#include <stdio.h>

int main() {
    int tempo, h, m, s;
    scanf("%d", &tempo);
    h = tempo/3600;
    tempo = tempo-(h*3600);

    m = tempo/60;
    tempo = tempo-(m*60);

    s = tempo;
    printf("%d:%d:%d\n", h, m, s);
    return 0;
}
