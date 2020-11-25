#include <stdio.h>
void main(){
    char test[] = "suat";
    char *tp = test;
    for (int i = 0; i < sizeof(test); i++){
        printf("%c", *(tp+i));
    }
}