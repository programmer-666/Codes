#include <stdio.h>
#include <stdlib.h>
int main(){
	char *p[] = {"one", "two"};
	int i[] = {34,48,26};
	printf("%s %d", p[0], i[1]);
	return 0;
}