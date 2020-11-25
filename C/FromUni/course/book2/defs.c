#include <stdio.h>
#define kare(x) (x*x)

int main(){
    printf("%d", kare(kare(2)));
    return 0;
}