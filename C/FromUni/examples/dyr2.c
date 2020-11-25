#include <stdio.h>
#include <stdlib.h>

void main(){
    int *p;
    p = (int *) malloc(10*sizeof(int));
    *(p+0) = 12;
    *(p+1) = 24;
    printf("%d %d", *(p+0), *(p+1));
    free(p);
}