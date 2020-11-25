#include <stdio.h>
void main(){
    unsigned char fbe[] = {'a', 'b', 'c'};
    unsigned char *fb = fbe;
    printf("%c %x\n", fbe[0], &fbe[0]);
    printf("%x %x\n", fbe, &fbe);
    printf("%c %c %c %c\n", *fb, *fb+1, *fb+2, *fb+5);
}