#include <stdio.h>
void main(){
    int a = 10;
    int *p;
    p = &a;
    printf("%d %d %d %d %d\n", *p, p, &p, a, &a);
}
