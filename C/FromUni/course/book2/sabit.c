#include <stdio.h>
#define x 3.24235323233
// ikisi de sabit fark yok
int main(){
    const float y = 3.14;
    printf("%f, %f, %f", x, y, x*y);
    return 0;
}