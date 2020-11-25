#include <stdio.h>
#include <stdlib.h>

int main(void){
    // katarları dosyaya yazmak için fputs, okumak için fgets() kullanılır.
    FILE *file = fopen("data.txt", "r");
    char *katar = (char*)malloc(128);
    if (file){
        while (fgets(katar, 7, file)){
            printf("%s", katar);
        }
    }
    fclose(file);
    puts("\n");
    // read
    FILE *file2 = fopen("test.data", "w");
    if (file2){
        char *strx = "Test data";
        fputs(strx, file2);
    }
    fclose(file);
    // write
    return 0;
}