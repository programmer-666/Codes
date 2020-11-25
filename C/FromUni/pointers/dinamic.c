#include <stdio.h>
#include <stdlib.h>

int main(){
    //malloc, calloc, realloc gibi komutlarla yer tayin edilir. Byte cinsinden yer ayrilir.
    int *p = (int*)malloc(10*sizeof(int));
    *(p+0) = 3;
    *(p+1) = 2;
    int *y = qrr();
    printf("%d %d %d %ld %d", *p, *(p+1), *(p+0)+*(p+1), sizeof(*p)*10, *y);
    return 0;
}

int *qrr(){
    int *x, b = 3;
    x = &b;
    return x;
}