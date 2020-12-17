#include <stdio.h>
#include "testheader.h"

int sq(int a); // prototype
int main(){
    printf("%d %d", sq(2), sqr(2));
    return 0;
}
int sq(int a){return a*a;} // function 