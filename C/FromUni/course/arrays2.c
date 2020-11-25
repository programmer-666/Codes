#include <stdio.h>
int main(){
    unsigned char test[] = {1,3,5,7};
    // dizi adı/veritibi = dizi boyutu
    printf("%d %d", sizeof(test), sizeof(char));
    return 0;
}