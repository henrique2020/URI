//a, b, c, r1, r2, delta = número 1, 2 e 3, resultado 1 e 2, raiz quadrada
#include <stdio.h>
#include <math.h>

int main() {
  double a, b, c, r1, r2;
  scanf("%lf %lf %lf", &a, &b, &c);
  double delta = b*b-4*a*c;
  if(a == 0 || delta < 0){
    printf("Impossivel calcular\n");
  }
  else{
    delta = sqrt(delta);
    r1 = (-b+delta)/(2*a);
    r2 = (-b-delta)/(2*a);
    printf("R1 = %.5lf\n", r1);
    printf("R2 = %.5lf\n", r2);
  }
  return 0;
}
