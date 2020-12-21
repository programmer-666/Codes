#include <stdio.h>
#include <stdlib.h>
int main(){
	unsigned char *s = (unsigned char*)malloc(5);
	s = "hello";
	printf("%X -> %s", &s, s);
	return 0;
}
