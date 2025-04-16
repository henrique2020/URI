// n1, n2, n3 = nota 1, 2 e 3
#include <stdio.h>

int main() {
  double n1, n2, n3, soma;
  scanf("%lf %lf %lf", &n1, &n2, &n3);
  soma = (n1*0.2)+(n2*0.3)+(n3*0.5);
  printf("MEDIA = %0.1lf\n", soma);
  return 0;
}
