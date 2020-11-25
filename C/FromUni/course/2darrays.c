#include <stdio.h>
int main(){
    int x[1][0], y[][3] = {1,2,3,4,5,6,7,8,9};
    x[0][0] = 3;
    x[1][0] = 2;
    int a = x[0][0]+x[1][0];
    printf("%d", y[0][2]);
    return 0;
}