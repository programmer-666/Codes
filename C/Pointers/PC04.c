#include <stdio.h>
#include <stdlib.h>
int main(){
	int *ip = (int *)malloc(sizeof(int)*10);
	int *ap;
	int a = 12;
	*(ip+0) = a;
	ap = &a;
	printf("%d->%d, %d, %X", *ip, a, *ap, ap);
	*ap = 21;
	printf("\n%d", a);
	return 0;
}
