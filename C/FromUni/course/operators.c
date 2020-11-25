#include <stdio.h>

int main(){
  register unsigned char x = 12;
  ++x;
  printf("%d\n", x);
  x++;
  printf("%d\n", x);
  return 0;
}
