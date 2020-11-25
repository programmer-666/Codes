#include <stdio.h>
#include <stdlib.h>

int main(){
    char *katar = (char*)malloc(10); // 10Bytelik katar. 1 adet null dahil 10 byte.
    katar = "Deneme";
    // 11 veya 12 karakter girilirse ne olur?
    // 11. ve 12. karakterleri barindiran bellek adresleri ezilir, sagliksiz bir islemdir dikkatli olunmalıdır.
    printf("%c", *(katar+1));
    return 0;
}