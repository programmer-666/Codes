#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int MAX = 20;
int main(){
    int *A = (int*)malloc(MAX*sizeof(int));
    float  ort = 0;
    char b = 0, k = 0;

    for (size_t i = 1; i <= MAX; i++){
        *(A+i) = rand()%MAX;
        ort += *(A+i)/i;
    }

    for (size_t i = 0; i < MAX; i++){
        if (*(A+i)<ort){
            k+=1;
        }else{
            b+=1;
        }
    }
    printf("%d %d ort: %f", b, k, ort);    
    return 0;
}