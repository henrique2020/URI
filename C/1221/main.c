//Time limit exceeded
#include <stdio.h>

int prime(int number){
    if (number == 2){ return 1; }
    else if (number == 2 || number == 1){ return 0; }
    else if (number%2 == 0){ return 0; }
    else{
        int i, len = (number+1)/2;
        for(i = 3; i < len; i+=2){
            if(number%i == 0){
                return 0;
            }
        }
        return 1;
    }
}

int main() {
    int number, rep;
    scanf("%d", &rep);

    while (rep){
        scanf("%d", &number);

        if(prime(number) == 0){
            printf("Not Prime\n");
        }
        else{
            printf("Prime\n");
        }
          
        rep -=1;
    }

    return 0; 
}
