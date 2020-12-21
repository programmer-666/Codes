#include <stdio.h>
int main(){
    char text[11] = "Hello World";
    unsigned char nums[2] = {22,33};

    printf("%s %d %d len-> %d", text, text, sizeof(text)/sizeof(char));
    printf("%d %d", nums, nums[0]);
    return 0;
}