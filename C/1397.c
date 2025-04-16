#include <stdio.h>

int main() {
    int rep, p1, p2, n1, n2;
    for (;;){
        scanf("%d", &rep);
        if(rep == 0){
            break;
        }

        p1 = 0, p2 = 0;
        while (rep){
            scanf("%d %d", &n1, &n2);
            if(n1 > n2){ p1+=1; }
            else if (n1 < n2){ p2 +=1; }
            rep-=1;
        }        
        printf("%d %d\n", p1, p2);
    }
    return 0;
}
