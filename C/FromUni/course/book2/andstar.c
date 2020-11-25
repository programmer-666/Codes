#include <stdio.h>
void main(){
    /*
    * karakteri genelde pointer bildirmede ve bu pointerin sakladigi bellekteki degeri getirmekte kullanilir.
    * & ise bir degiskenin adresini verir.
    */
   unsigned char *cp, *cp2, x = 3, *cp3 = cp;
   cp = &x;
   *cp2 = x;
   printf("%d %d", *cp, *cp2);
}