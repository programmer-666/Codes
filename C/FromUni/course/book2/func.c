#include "stdio.h"

float ort(int x, int x2){
  return (x+x2)/(x2/x);
}

int main(){
  printf("%0.2f\n", ort(1, 2));
  return 0;
}
