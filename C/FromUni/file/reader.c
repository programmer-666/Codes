#include <stdio.h>
#include <stdlib.h>

int main(void){
    FILE *file = fopen("data.txt", "r");
    while (!feof(file)){ // EOF - end of file | getc(file) != EOF other section
        putchar(getc(file));
    }
    fclose(file);
    return 0;
}