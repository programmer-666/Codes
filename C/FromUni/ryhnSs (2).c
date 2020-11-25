#include <stdio.h>
int main(){
    char no[11], name[7] = "REYHAN";
    printf("Ogrenci numaranizi giriniz:");scanf("%s", no);
    printf("Son dort rakaminiz:");
    int master = ( 10 * (no[7] - '0' ) ) + no[8] - '0', Ofpuppets = ( 10 * (no[9] - '0' ) ) + no[10] - '0';
    printf("%c%c%c%c\nSimdi isminiz %d defa yazilacak\n-------------------------------", no[7], no[8], no[9], no[10], master+Ofpuppets);
    for (int i = 1; i <= master+Ofpuppets; i++){printf("\n%d.kez merhaba %s", i, name);}
    return 0;
}
//19110011024