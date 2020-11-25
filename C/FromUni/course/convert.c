#include <stdio.h>

int main(){
	//Implicit 10 -> 100
	char x = 20;unsigned char b;int y;
	y = x;
	printf("%d\n", y);
	//Explicit 100 -> 10
	int z = 90, a = 198;
	y = (char)z;b = (char)a;
	printf("%d %d", y, b);
	return 0;
}
