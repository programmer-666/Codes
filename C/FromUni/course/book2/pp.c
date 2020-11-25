#include <stdio.h>
int main(){
    auto unsigned char x = 4;
    printf("%d\n", x);
    ++x;
    printf("%d\n", x);
    printf("%d\n", x++);
    printf("%d\n", x);
    return 0;
}