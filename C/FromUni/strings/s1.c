#include <stdio.h>
#include <string.h>

int main(){
    char k1[] = "Katar1";
    char k2[] = "Katar2";
    strcat(k1, k2);// k2 yi k1 e ekler
    printf("%s %s\n", k1, k2);
    printf("%d\n", strchr(k1, 'a'));
    return 0;
}