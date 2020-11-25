#include <stdio.h>
void main(){
    char x[2][3] = {{12,23,45},{34,12,56}};
    char y[2][3] = {{45,73,25},{14,124,55}};
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++){
            printf("%d\n", x[i][j]+y[i][j]);
        }
    }
}