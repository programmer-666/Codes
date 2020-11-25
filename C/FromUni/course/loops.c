#include <stdio.h>
int main(){
  char i = 0;
  for (register unsigned char i = 0; i < 128; i++) {
    printf("%d -> %c\n", i, i);
  }
  while(i<120){
    printf("%d\n", i);
    i+=1;
  }
  //do while ise önce işlemi yapar sonra ifade sorgulanır
  return 0;
}
