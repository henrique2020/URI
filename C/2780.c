#include <stdio.h>

int main() {
    int d, p;
    scanf("%d", &d);
    if (d <= 800) { p = 1; } 
    else if (d <= 1400) { p = 2; } 
    else { p = 3; }

    printf("%d\n", p);
    return 0;
}
