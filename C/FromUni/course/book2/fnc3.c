#include <stdio.h>
int pf(int a, int b){
    return a+b;
}
void main(){
    int (*f)(int,int);
    f = pf;
    printf("%d", f(1,2));
 }