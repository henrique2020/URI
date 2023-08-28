#include <stdio.h>

int main() {
    int n1, n2;
    scanf("%d\n%d", &n1, &n2);
    if(n1%2 == 0 && n2%2 == 0){
        printf("%d\n", 1);
    } else if (n1%2 != 0 && n2%2 != 0) {
        printf("%d\n", 1);
    } else {
        printf("%d\n", 0);
    }

    return 0;
}