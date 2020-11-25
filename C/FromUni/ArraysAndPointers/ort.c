#include <stdio.h>
#include <stdlib.h>

int main(){
    int n[2];
    n[0] = 2;
    n[1] = 3;
    n[2] = 3;
    printf("%f %d", (float)(n[0]+n[1]+n[2])/3, fnc(n));
    return 0;
}
int fnc(int d[2]){
    return d[0]+d[1];
}