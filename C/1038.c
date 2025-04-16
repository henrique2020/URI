#include <stdio.h>

int main(void) {
  int cod;
  int quantidade;
  scanf("%d%d", &cod, &quantidade);
  float valor[5] = {4.00, 4.50, 5.00, 2.00, 1.50};
  printf("Total: R$ %.2f\n", (quantidade*valor[(cod-1)]));
  return 0;
}
