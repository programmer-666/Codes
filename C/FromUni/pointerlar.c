#include <stdio.h>

int main(){
    char x = 3, *p;
    p = &x;
    for (size_t i = 0; i < 3; i++){
        p+=i;
        printf("%c %d\n", *p, p);
    }
    
    return 0;
}