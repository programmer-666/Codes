#include <stdio.h>
#include <stdlib.h>

int main(){
    int x[10];// 40 Byte Array (int = 4Byte)
    printf("%X %d %ld", x, x[0], sizeof(x));
    return 0;
}