#include <stdio.h>

int main() {
    char phrase[] = "LIFE IS NOT A PROBLEM TO BE SOLVED";
    int len, i;
    scanf("%d", &len);
    for(i = 0; i < len; i++){ printf("%c", phrase[i]); }
    printf("\n");
    return 0;
}
