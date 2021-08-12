#include <stdio.h>

int main() {
  double n1, n2, n3, soma;
  scanf("%lf", &n1);
  scanf("%lf", &n2);
  scanf("%lf", &n3);
  soma = (n1*0.2)+(n2*0.3)+(n3*0.5);
  printf("MEDIA = %0.1lf", soma);
  puts("");

  return 0;
}
