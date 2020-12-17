#include <stdio.h>

int main(){
    for(register unsigned char i = 33;i<127;i++)
        printf("%c", i);
    printf("\n");
    unsigned char x = 1;
    while(x<10){
        if (x%4 == 0){
            printf("\n");
        }else{
            printf("%d", x);
        }
        x++;
    }
    printf("\n");
    unsigned char a = 0;
    do{
        a++;
        printf("hello.");
    } while (0);
    
    return 0;
}