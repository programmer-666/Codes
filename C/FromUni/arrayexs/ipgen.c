#include <stdio.h>
#include <stdlib.h>
#include <math.h>
long count = 0;
void main(){
    unsigned char *ip = (char*)malloc(3);
    for (unsigned char x = 0; x < 255; x++){
        *ip = x;
        count+=1;
        for (unsigned char a = 0; a < 255; a++){
        *(ip+1) = a;
        count+=1;
        for (unsigned char i = 0; i < 255; i++){
            *(ip+2) = i;
            count+=1;
            for (unsigned char j = 0; j < 255; j++){
                count+=1;
                *(ip+3) = j;
                //printf("%d.%d.%d.%d\n", *ip, *(ip+1), *(ip+2), *(ip+3));
            }
        }
    }
    }
    printf("%ld", count);    
}

