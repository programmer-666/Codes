#include <stdio.h>
void main(){
    //pointerlar değişkenlerin bellek adreslerini taşırlar
    unsigned char test = 34;
    printf("%d (%X)16 = (%d)10", test, &test, &test);
    //bir değişkenin (bellekte yer kaplayan nesnenin) adresini öğrenmek için & kullanılır 
}