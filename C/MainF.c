#include <stdio.h>

void main(int args, char *argv[]){
    for (size_t i = 1; i < args; i++){
        printf("%s", argv[i]);
    }
}