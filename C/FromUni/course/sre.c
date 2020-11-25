#include <stdio.h>
#define pi 3.141592653589793
int main(){
    float r;
    printf("r: ");scanf("%f", &r);
    printf("%f", (4*pi*(r*r*r))/3);
}