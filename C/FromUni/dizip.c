#include <stdio.h>

int main(){
    int dizi[10], *p;
    p = dizi;
    dizi[3] = 33;
    printf("%d", *(p+3));
    return 0;
}