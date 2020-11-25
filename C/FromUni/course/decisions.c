#include <stdio.h>

int main(){
  char x = 3, y = 4, z = 1;
  if(x|y>z){
    printf("x|y>z -> %d\n", x|y);
  }
  if(x == 0){
    printf("1\n");
  }else if(x^y == x|y){
    printf("x|y==x^y\n");
  }else{
    printf("0\n");
  }
}
