//a, b, c, r1, r2, raizQ = número 1, 2 e 3, resultado 1 e 2, raiz quadrada
#include <stdio.h>
#include<math.h>

int main() {
  double a, b, c, r1, r2, raizQ;
  scanf("%lf %lf %lf", &a, &b, &c);
  raizQ = sqrt(b*b-4*a*c);
  if(a != 0 && raizQ >= 0){
    r1 = (-b+raizQ)/(2*a);
    r2 = (-b-raizQ)/(2*a);
    printf("R1 = %.5lf\n", r1);
    printf("R2 = %.5lf\n", r2);
  }
  else{
    printf("Impossivel calcular\n");
  }
  return 0;
}
