#include <stdio.h>
#include <math.h>
int main(){
    int n, t = 0;
    printf("N=");scanf("%d", &n);
    for (int i = 0; i <= n; i++){
        t+=pow(3, i)-2*i+5;
    }
    printf("%d", t);
    return 0;
}
