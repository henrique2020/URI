#include <stdio.h>

int main(void) {
  int hI, mI, hF, mF;
  scanf("%d%d%d%d", &hI, &mI, &hF, &mF);

  int horas, minutos;
  if (hI > hF){
    horas = 24 - (hI-hF);
  }
  else if (hI < hF){
    horas = hF - hI;
  }
  else{
    if(mI >= mF){
      horas = 24;
    }
    else{
      horas = 0;
    }
  }

  if (mI > mF){
    horas --;
    minutos = 60 - (mI-mF);
  }
  else if (mI < mF){
    minutos = mF - mI;
  }
  else{
    minutos = 0;
  }

  printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", horas, minutos);
  return 0;
}
