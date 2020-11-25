#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float discriminant(float a, float b, float c){return pow(b, 2)-4*a*c;}

void main(){
    float nums[10];
    unsigned char r = 10;
    for (register unsigned char i = 0; i < 30; i++){
        printf("%f\n", discriminant(rand()%rand()%r, rand()%rand()%r, rand()%rand()%r));
    }
}