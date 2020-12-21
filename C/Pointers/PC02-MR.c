#include <stdio.h>
#include <stdlib.h>
int main(){
	char *str = (char*)malloc(6);
	//str = "HELLO";
	// READING MEM
	for(size_t i = 0;i<1024;i++)
		printf("%c", *(str+i));
	return 0;
}
