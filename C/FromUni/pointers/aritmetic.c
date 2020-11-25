#include <stdio.h>
#include <stdlib.h>

int sizefinder(int *p){
    int *c = p;
    while(*c != 0){
        c++;
    }
    return (c-p)/sizeof(int);
}

int main(){
    int *p, x[4] = {3, 33, 32, 31};
    p = x;
    printf("%d %d", sizefinder(p), *(p+1));
    /*
    int 4B
    yani p nin aldigi deger 400 varsayalim
    p++ ifadesinden sonra yeni deger 404 olacaktir.
    p++ = > p = p + sizeof(int)
    p+=n = > p = p + n * sizeof(int)    
    */
    return 0;
}