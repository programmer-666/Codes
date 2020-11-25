#include <stdio.h>
#include <stdlib.h>

int main(void){
    FILE *filew = fopen("data.csv", "w");
    FILE *filer = fopen("data.csv", "r");
    int x, y;
    fprintf(filew, "%d,%d", 1, 12);
    fclose(filew);
    while (!feof(filer)){
        fscanf(filer, "%d,%d", &x, &y);
        printf("%d,%d", x,y);
    }
       
    fclose(filer);
    return 0;
}