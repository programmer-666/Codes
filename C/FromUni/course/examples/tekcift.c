#include <stdio.h>

int main(){
    int data[100];
    int x = 0; 
    for (register int i = 0; i < 100; i++){
        if (i%2 == 1){
            data[x] = i;
            x+=1;
        }
    }
    for (int i = 0; i < x; i++){
        printf("%d - %d\n", data[i], i);
    }
    return 0;
}