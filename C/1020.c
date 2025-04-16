//Ano, mês = 365 e 30 dias || vida = total de dias
#include <stdio.h>

int main() {
    int vida, ano, mes, dia;
    scanf("%d", &vida);

    ano = vida/365;
    mes = (vida-(ano*365))/30;
    dia = ((vida-(ano*365))-mes*30);

    printf("%d ano(s)\n", ano);
    printf("%d mes(es)\n", mes);
    printf("%d dia(s)\n", dia);
    return 0;
}
