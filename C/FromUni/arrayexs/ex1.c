#include <stdio.h>
#include <stdlib.h>

char g_v = 0;

void cahc(void){
    g_v = 3;
}

void main(){
    printf("%d", g_v);
    cahc();
    printf("%d", g_v);
}

