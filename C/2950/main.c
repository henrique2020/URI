#include <stdio.h>

int main(void) {
  int distancia, sauron, saruman;
  scanf("%d%d%d", &distancia, &sauron, &saruman);
  float icm = (distancia+0.0)/(sauron+saruman);
  printf("%.2f\n", icm);

  return 0;
}
