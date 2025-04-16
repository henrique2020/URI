#include <stdio.h>

int main(void) {
  int fO, fA;
  while(1){
    scanf("%d", &fO);
    scanf("%d", &fA);

    if(fO == 0 && fA == 0){
      break;
    }
    else{
      printf("%d\n", fO+fA);
    }
  }
  return 0;
}
