#include <stdio.h>
#include <math.h>

void main(){
    //Sayısal ve sözel fonksiyonlar
    //math.h -> matematiksel fonksiyonları içerir
    float exf = 2.31415982;
    char exc = -4;
    printf("%f\n", sqrt(exf));// karekök
    printf("%f\n", pow(exf, sqrt(exf)));// üs
    printf("%f\n", fabs(exc));// mutlak
    printf("%f\n", floor(exf));// en yakın küçük int
    printf("%f\n", ceil(exf));// en yakın büyük int
    printf("%f\n", sin(exf));// sinüs
    printf("%f\n", cos(exf));// cosinüs
    printf("%f\n", log(exf));// e tabanına göre log
    printf("%f\n", exp(exf));// e sabitinin exf. kuvvet
    printf("%f\n", fmod(exf, exc));// exf'in exc'ye bölümünden kalan
}