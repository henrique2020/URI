#include <stdio.h>

int main() {
    char ho[3] = "Ho";
    int rep, i;
    scanf("%d", &rep);

    for(i = 1; i < rep; i++) {
        printf("%s ", ho);
    }

    printf("%s!\n", ho);
    return 0;
}
