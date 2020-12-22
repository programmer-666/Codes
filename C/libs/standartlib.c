#include <stdio.h>
#include <stdlib.h>
#define XV rand()%128 // RANDOM_INTEGER_FROM_STDLIB
//void qe(void);
int main(){
	char *ptr = (char*)malloc(11);
	char *fptr = (char*)malloc(3);
	fptr = "3.14";
	ptr = "HELLOWORLD";
	system("cls");
	printf("%d %s %f", XV, ptr, atof(fptr));
	//at_quick_exit(qe);
	//quick_exit(EXIT_SUCCESS);
	return 0;
}
/*void qe(void){
	printf("quick exiting");
	fflush(stdout);
}*/
