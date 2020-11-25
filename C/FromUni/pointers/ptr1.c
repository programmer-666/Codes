#include <stdio.h>
#include <stdlib.h>

int main(){
    // Pointer bellekteki bir alanin gozunun saklandigi degiskendir. Verilerin baslangic adreslerini tutarlar.
    int x = 3, *xp;
    xp = &x; // & isareti degiskenin adresini verir.
    printf("%d", *xp); // x degiskeninideki deger yazdirildi.
    return 0;
}