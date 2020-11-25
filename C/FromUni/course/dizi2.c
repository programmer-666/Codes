#include <stdio.h>

int main(){
  int x[5][5];
  int y[5][5][10];
  printf("%d %d %d\n", 5*5*sizeof(int), sizeof(x), sizeof(y));
  return 0;
}
