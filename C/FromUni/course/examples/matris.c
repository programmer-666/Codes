#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX 4
void main(){

    char matris[MAX][MAX];
    for (register unsigned char i = 0; i < MAX; i++){
        for (register unsigned char j = 0; j < MAX; j++){
            matris[i][j] = rand()%127;
        }
    }

    for (register unsigned char i = 0; i < MAX; i++){
        for (register unsigned char j = 0; j < MAX; j++){
            printf("matris[%d][%d] = %d\n", i, j, matris[i][j]);
        }
    }
}