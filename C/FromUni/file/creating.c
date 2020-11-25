#include <stdio.h>
#include <stdlib.h>

void main(void){
    FILE *file = fopen("veriler.data", "w");
    if (file != NULL){
        printf("File created.");
        fclose(file);
    }else{
        printf("File not created.");
        fclose(file);
    }
}