#include <stdio.h>
void main(){
    //pointer tanımlama
    char x = 3;
    char *p1 = &x;
    printf("x: %x %x", x, &x);
    printf("\np1: %x %x", p1, &p1);
}