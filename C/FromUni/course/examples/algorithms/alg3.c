#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    // girilen katarin ortalamasini bulan program
    char katar[] = "this is a lorem text test";
    float total = 0;
    register unsigned char i = 0;
    for (; i < sizeof(katar)/sizeof(char); i++){
        total+=katar[i];
    }
    printf("%0.2f %0.2f", total, total/i);
    
    
    return 0;
}