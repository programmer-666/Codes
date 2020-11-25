#include <stdio.h>

int main(){
  int x[] = {12, 34, 54 ,12, 22};
  for (int i = 0; i < sizeof(x)/sizeof(int); i++) {
    printf("%d\n", x[i]);
  }
  return 0;
}
