#include <stdio.h>
int main(){
    char nums[] = {4,3, -2,4,5,3,2,3,4,5,7,63, 'a', 'b'};
    char biggest = 0, smallest = nums[0];
    for (register unsigned char i = 0; i < sizeof(nums)/sizeof(char); i++){
        biggest = nums[i];
        if (nums[i]>biggest){
            biggest = nums[i];
        }
        if(nums[i]<smallest){
            smallest = nums[i]; 
        }
    }
    printf("%d %d", biggest, smallest);    
    return 0;
}