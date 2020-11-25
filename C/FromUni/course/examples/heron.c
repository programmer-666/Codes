#include <stdio.h>
#include <math.h>

float trs(float a, float b, float c){
    return (a+b+c)/2;
}
float area(float s, float a, float b, float c){
    return sqrt((s*(s-a)*(s-b)*(s-c)));
}

int main(){
    float a = 3.14, b = 2.71, c = 10;
    printf("%0.3f", (float)area(trs(a, b, c), a, b ,c));
    return 0;
}