#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    // fiyata kdv ekleyerek yazdir 
    float ft = 10+rand()%21;
    float oft = ft;
    ft = ft + ft*0.18;
    printf("%0.2f -> %0.2f",oft,  ft);
    return 0;
}