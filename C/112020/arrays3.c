#include <stdio.h>
int main(){
    unsigned char chr[11];
    unsigned char r;
    unsigned char ts[] = {'t', 's', '\0'};printf("%s\n", ts);
    for(char i = 0;i<11;i++){
        chr[i] = i+i;
        printf("%d\n", chr[i]);
    }
    printf("%d %d\n", chr[1], chr[10]);
    r = chr[1];
    chr[1] = chr[10];
    chr[10] = r;
    printf("%d %d\n", chr[1], chr[10]);
    return 0;
}