#include <stdio.h>
#include <math.h>
int main(){
    long total = 0, i = 0, dx = 0;
    while (1==1){
        printf("\n:");
        //scanf("%d", &dx);
        dx = (rand()%2);
        total+=dx;
        i+=1;
        printf(" %d : %d = %0.35f", total, i, (float)total/i);
        //printf("%0.35f", (float)total/i);
    }
    return 0;
}