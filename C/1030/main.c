//Incompletop

#include <stdio.h>

int main() {
    int rep, i, p, s;
    scanf("%d", &rep);
    for(i = 0; i < rep; i++){
        scanf("%d %d", &p, &s);
        int arr[p], j;
        for (j = 0; j < p; j++){ arr[j] = j+1; }

        for (;;){
            int len = sizeof(arr)/sizeof(arr[0]);
            if(len == 1){ break; }
            if(len >= s){}
            else{}
        }
        
        printf("%d\n",p%s);
    }
    return 0;
}
