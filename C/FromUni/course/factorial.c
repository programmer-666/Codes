#include "stdio.h"
int main(){
  // 5 -> 120 = 5.4.3.2.1
  register unsigned char i = 1, a = 1;
  while(i<5){i+=1;a = a*i;}
  printf("%d\n", a);
  return 0;
}
