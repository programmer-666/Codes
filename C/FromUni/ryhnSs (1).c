#include <stdio.h>
int main(){
    int n, t = 0, c = 0;
    printf("N Sayisi=");
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if ((i*j)%2!=0){
                t= t+1;
            }else{
                c=c+1;
            }
        }
    }
    printf("TEK=%d, CIFT=%d", t,c);
    return 0;
}
