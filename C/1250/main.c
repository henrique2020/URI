//rep, mov, ace = repetições, movimentos, vezes que ele é atingido
#include <stdio.h>
#include <stdlib.h>

int main() {
  int rep, mov, ace, i;
  scanf("%d", &rep);

  int arr[rep];
  for(i = 0; i < rep; i++){
    int i2;
    scanf("%d", &mov);

    int tiro[mov+1];
    for(i2 = 1; i2 < (mov+1); i2++){
      scanf("%d", &tiro[i2]);
    }

    char pulo[mov];
    scanf("%s", &pulo[0]);

    ace = 0;
    for(i2 = 0; i2 < mov; i2++){
      if((tiro[i2+1] <= 2 && pulo[i2] == 'S') || (tiro[i2+1] > 2 && pulo[i2] == 'J')){
        ace++;
      }
    }
    arr[i] = ace;
  }
  for(i = 0; i < rep; i++){
    printf("%d\n", arr[i]);
  }
  return 0;
}
