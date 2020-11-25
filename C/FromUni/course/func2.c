#include <stdio.h>
int x = 3;
void chc(){
  x = 5;
}
int main(){
  printf("%d\n", x);
  chc();
  printf("%d\n", x);
  return 0;
}
