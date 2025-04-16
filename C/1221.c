#include <stdio.h>
#include <math.h>

int prime(int number){
    int i;
    if (number%2 == 0 && number>2) { return 0; }

    for(i = 3; i < sqrt(number)+1; i+=2){
        if (number % i == 0) { return 0; }
    }

    return 1;
}

int main() {
    int number, rep;
    scanf("%d", &rep);

    while (rep){
        scanf("%d", &number);

        if(prime(number) == 0){ printf("Not Prime\n"); }
        else{ printf("Prime\n"); }

        rep -=1;
    }

    return 0;
}
