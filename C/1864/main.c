#include <stdio.h>

/*
-- Retorno algum erro só no URI... provavelmente devido a diferenças de versão. Parece que estoura a memória
int main() {
    char phrase[] = "LIFE IS NOT A PROBLEM TO BE SOLVED";
    int len;
    scanf("%d", &len);
    char view[len+2];

    strncpy(view, phrase, len);
    printf("%s\n", view);
    return 0;
}
*/

int main() {
    char phrase[] = "LIFE IS NOT A PROBLEM TO BE SOLVED";
    int len, i;
    scanf("%d", &len);
    for(i = 0; i < len; i++){ printf("%c", phrase[i]); }
    printf("\n");
    return 0;
}
