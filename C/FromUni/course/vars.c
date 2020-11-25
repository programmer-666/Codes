#include <stdio.h>

int main(){
    char x = 97;//-128 - 127 arası
    unsigned char a = 243;//Max 0-255
    unsigned long t = 12000*12000;
    double c = 3.14;
    printf("%4d %c %0.3f %3d", t, x, c, x);
    /*
    d işaretli tamsayı
    u işaretsiz tamsayı
    f noktalı
    e bilimsel gösterimli
    s string
    x onaltılık
    c karakter
    */
}