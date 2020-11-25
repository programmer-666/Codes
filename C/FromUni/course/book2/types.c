#include <stdio.h>

void main(){
    char hex = 0x1e;
    char oct = 036;
    char x = 30;
    int a = 1000UL;
    printf("%d %d %d %d %ld", hex, oct, x, a, sizeof(a));
}