#include <stdio.h>
void main(){
    char i = 0, *vp = &i;
    for (i = 0; i < 250; i++){
        vp+=i;
        printf("%d %x\n", *vp,  vp);
    }
}