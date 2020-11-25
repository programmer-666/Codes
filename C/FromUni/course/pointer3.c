#include <stdio.h>
void main(){
    char x = 'a';
    char *xp = &x;
    printf("%d %x", *xp, xp);
    xp++;
    printf("\n%d %x", *xp, xp);
}