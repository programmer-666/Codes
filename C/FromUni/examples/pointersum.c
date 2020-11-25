#include <stdio.h>

int asum(int array[], int n){
    int *p, t = 0;
    p = array;
    for (size_t i = 0; i < n; i++){
        t+=*(p+i);
    }
    return t;
}

int main(){
    int dizi[] ={1,3,5,7,9,11,13};// 7^2 = 49
    printf("%d", asum(dizi, sizeof(dizi)/sizeof(int)));
    return 0;
}