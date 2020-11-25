#include <stdio.h>

int main(){
  long f = 1;
  for (int i = 1; i <= 5; i++){f*=i;}
  printf("%ld\n", f);
  return 0;
}
/*
5! = 5*4*3*2*1
*/
