#include <stdio.h>
#include <stdlib.h>
int main(){
	char *str = (char*)malloc(6);
	str = "hello";
	/*printf("%s\n", str);
	putchar(*(str+0));
	printf("\n\n\n");*/
	// reading ram
	for(size_t i = 6;i<1024;i++)
		printf("%c", *(str+i));
	return 0;
}
