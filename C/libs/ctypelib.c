#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main(){
    char *s = (char*)malloc(11);
    s = "HELLOWORLD";
    printf("%s", s);
    return 0;
}