#include <stdio.h>
int main(){
    char x = 3;
    if (x == 4){
        printf("1");
    }else{
        printf("0");
    }
    switch (x){
    case 3:
        printf("1");
        break;
    
    default:
    printf("0");
        break;
    }
    
    return 0;
}