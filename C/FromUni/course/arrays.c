#include <stdio.h>

int main(){
  char ary[2], ary2[] = {1,3};
  ary[0] = 3;
  ary[1] = 2;
  ary[2] = 8;
  printf("%d %d %d - %d %d", ary[0], ary[1], ary[2], ary2[0], ary2[1]);
  return 0;
}
