#include <stdio.h>
#include <stdbool.h>
#include <math.h>
//Media aritmetica tra 2 numeri scelti dall'utente

int main()
{
    int Primo_Numero;
    int Secondo_Numero;
    printf("Ciao utente, inserisci un numero:");   
    scanf("%d", &Primo_Numero);
    printf("Grazie! Se inserisci un altro numero, faccio la media aritmetica per te:");
    scanf("%d", &Secondo_Numero);
    float Media = (float(Primo_Numero) + float(Secondo_Numero)) / 2;
    printf("%f", Media);

}