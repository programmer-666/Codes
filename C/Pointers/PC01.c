#include <stdio.h>
#include <stdlib.h>
int main(){
	int *intP = (int*)malloc(sizeof(int)*1);
	*(intP+0) = 1024;
	printf("%d %d", *intP, *(intP+1));
	return 0;
}
