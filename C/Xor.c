#include <stdio.h>
#include <stdlib.h>
#define PSIZE   32
int main(void){
    // Size
    char *passw = (char *) malloc(PSIZE);    
    if (scanf("%s", passw) == 1){
        for (unsigned char i = 0; i < PSIZE; i++){
            *(passw+i) = *(passw+i)^(PSIZE+i);
        }
        printf("%s", passw);
    }
    // Password Input
    return 0;
}
