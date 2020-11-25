#include <stdio.h>
#include <stdlib.h>

int main(){
    char *p = (char *)malloc(11);
    p = "Deneme";
    printf("%s %c", p, *p);
    return 0;
}<