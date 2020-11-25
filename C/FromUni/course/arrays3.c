#include <stdio.h>
int main(){
    unsigned char x[] = {1,2,2,3,5,3,2,4,65,7,52,34,6,8,5,3};
    for (register unsigned char i = 0; i < sizeof(x)/sizeof(char); i++){
        printf("%d -> %d\n", i, x[i]);
    }
    
    return 0;
}