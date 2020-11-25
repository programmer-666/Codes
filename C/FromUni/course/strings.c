#include <stdio.h>
#include <string.h>

int main(){
    char str[100] = "Hello";
    char str2[100] = "World";
    printf("%ld\n", strlen(str));//string uzunlugunu yazar \0 haric
    printf("%s\n", strcpy(str, str2));//string uzunlugunu yazar \0 haric
    printf("%s\n", strcpy(str, str2));//string uzunlugunu yazar \0 haric
    printf("%s\n", strncpy(str, str2, 2));// str2 nin ilk n karakterini str ye kopyalar
    printf("%s\n", strcat(str, str2));// str nin sonuna str2 yi ekler
    printf("%d\n", strcmp(str, str2));// iki metni karşılaştırır aynıysa 0 doner
    printf("%s\n", strstr(str, str2));// str içinde str2 yi arar bulamazsa null doner
    return 0;
}