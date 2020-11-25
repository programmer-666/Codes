#include <stdio.h>
#include <stdlib.h>

int main(){
    unsigned long *ry;
    ry = malloc(2);
    free(ry);
    return 0;
}