#include <stdio.h>

int main(){
    unsigned char x = 3;
    char a[1024];
    printf("%ld %ld", sizeof(x), sizeof(a));//boyutu gosterir
    return 0;
}