#include <stdio.h>

int main(){
    for (register unsigned short i = 0; i < 128; i++)
        printf("%c\n", i);
    return 0;
}