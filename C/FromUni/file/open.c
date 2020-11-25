#include <stdio.h>
#include <stdlib.h>

void main(void){
    FILE *file = fopen("veriler.data", "r");
    
    fclose(file);
}