#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    // 2 farkli sayidan buyuk olani bul
    int x = rand()%10, y = rand()%10;
    if (x > y){
        printf("%d", x);
    }else if (y > x){
        printf("%d", y);
    }else{
        printf("%d=%d", x, y);
    }
    
    return 0;
}