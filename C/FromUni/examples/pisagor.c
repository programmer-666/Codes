#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void main(){
    int *p;
    p = (int *) malloc(1*sizeof(int));// 1 elemana gore ayrilan yere birden fazla deger atanirsa zaman zaman hatalarla karsilasilabilir. saglikli bir durum degildir...
    *p = 3;
    *(p+1) = 12;
    *(p+2) = 13;
    *(p+3) = 23;
    printf("%d", sizeof(p)/sizeof(int));
}