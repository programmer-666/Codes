#include <stdio.h>
int main(){
    int a[] = {2,4,6,8,0};
    char t[] = "JNYSHND";
    printf("%d %d", sizeof(a)/sizeof(int), sizeof(t)/sizeof(char));
    printf("%s", t);
    return 0;
}