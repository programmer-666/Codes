#include <stdio.h>
void main(){
    unsigned char datas[1][1];
    for (register unsigned char i = 0; i <= 1; i++){
        for (register unsigned char j = 0; j <= i; j++){
            printf("%d %d\n", i, j);
        }
        
    }
    
}