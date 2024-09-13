#include <stdio.h>
#include <stdbool.h>
#include <math.h>
//Moltiplicazione tra 2 numeri scelti dall'utente

int main()
{
    int Primo_Numero;
    int Secondo_Numero;
    printf("Ciao utente, inserisci un numero:");   
    scanf("%d", &Primo_Numero);
    printf("Grazie! Se inserisci un altro numero, faccio una moltiplicazione per te:");
    scanf("%d", &Secondo_Numero);
    int Prodotto = Primo_Numero * Secondo_Numero;
    printf("%d", Prodotto);

}