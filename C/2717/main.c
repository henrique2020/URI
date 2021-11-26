#include <stdio.h>

int main(void) {
  int fimExp, pre1, pre2;
  scanf("%d%d%d", &fimExp, &pre1, &pre2);
  if(fimExp >= (pre1+pre2)){
    printf("Farei hoje!\n");
  }
  else{
    printf("Deixa para amanha!\n");
  }
  return 0;
}
