#include <stdio.h>
#include <ctype.h>// Karakter fonksiyonlari

int main(){
    register unsigned char primary = 97;
    printf("%d\n", isalnum(primary));// Girilen deger harf veya rakamdan farkliysa 0 dondurur
    printf("%d\n", isalpha(primary));// Girilen deger harf ise 0 dan fakli bir deger dondurur - alfanumerik mi
    printf("%d\n", isdigit(primary));// rakammi
    printf("%d\n", islower(primary));// kucuk harf mi
    printf("%d\n", isupper(primary));// buyuk harf mi
    printf("%d\n", isspace(primary));// bosluk tab veya yani satir mi
    printf("%d\n", tolower(primary));// kucuk harf yapar
    printf("%d\n", toupper(primary));// buyuk harf yapar
    return 0;
}